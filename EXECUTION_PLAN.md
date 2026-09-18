# Execution plan — how to run this fast

**Written:** 2026-09-07. **Status:** analysis complete, nothing applied.

**Scope note.** The findings below were measured by reading the implementation repo at
`~/Desktop/equity reserch` on 2026-09-07. That read was **read-only**; nothing in that repo was
modified. Every file:line reference points there. Applying any of this is a decision for that repo's
owner, taken in that repo's own session — not from here.

---

## 1. Where the time actually goes — measured, not guessed

### 1.1 Zero parallelism anywhere

`src/firm/core/pipeline/deep_dive.py:1309` is a plain serial loop:

```python
for name, (spec, system, user) in packets.items():
```

Each iteration reaches a blocking `subprocess.run(...)` at
`src/firm/core/llm/provider.py:140`, shelling out to headless `claude -p` with a 300 s ceiling
(`config/models.yaml: timeouts.default_seconds`).

Grep across the pipeline and provider for `asyncio|ThreadPool|ProcessPool|concurrent|gather` returns
**nothing**. With 14 agents in the roster, the worst case is 14 × 300 s ≈ **70 minutes of wall-clock per
company** in the agent phase alone. The one real measurement in the repo — the bank AR packet at 341 s —
confirms agents take minutes, not seconds.

**The fix is contained.** `config/roster.yaml` already groups the 14 agents into **7 stages** and
documents "agents run in stage order, then in listed order within a stage". The grouping exists; only
the concurrency is missing. No stage holds more than 3 agents. The subprocess runner is injectable
(`self._runner` in `ClaudeCodeAdapter`), so a `ThreadPoolExecutor` keyed by stage is unit-testable
without the CLI installed.

| | agent-phase wall clock |
|---|---|
| today (serial, 14 calls) | up to ~70 min; realistically 28–45 min |
| by-stage concurrency (7 barriers) | ~7 × slowest-in-stage |

*Estimate, not a measurement: derived from the 300 s ceiling and the single 341 s datapoint. The first
parallel run gives the real number.*

### 1.2 The model roles were never filled in

`config/models.yaml` ships literal placeholders:

```yaml
roles:
  extraction:     { model: "<cheap-model>",   temperature: 0.0, max_output_tokens: 2000 }
  classification: { model: "<cheap-model>",   temperature: 0.0, max_output_tokens: 1000 }
  analysis:       { model: "<mid-model>",     temperature: 0.2, max_output_tokens: 4000 }
  synthesis:      { model: "<strong-model>",  temperature: 0.3, max_output_tokens: 8000 }
  red_team:       { model: "<strong-model>",  temperature: 0.4, max_output_tokens: 6000 }
  valuation:      { model: "<strong-model>",  temperature: 0.1, max_output_tokens: 6000 }
```

under a note reading *"placeholders to be confirmed with the human (PLAN OQ#5) before Phase 2."*
Phase 2 shipped; this never happened. So `transcript_analyst` (role `extraction`, temp 0.0, 2 000
tokens) runs on the same model as `red_team`.

**The cheap/strong split is fully architected and entirely unused.** Filling in three strings is the
cheapest available win. Suggested, pending owner sign-off since it changes cost:

| role | model |
|---|---|
| `extraction`, `classification` | Haiku 4.5 |
| `analysis` | Sonnet 5 |
| `synthesis`, `red_team`, `valuation` | Opus 5 |

*Note: `docs/directives/` sets a model floor of Opus 4.8+ for **implementation work on the repo**. That
is a different axis from the model each pipeline agent runs on. The two do not conflict.*

### 1.3 Rework dominates, not throughput

From `state/progress.json` on 2026-09-07:

| unit | status | attempts | note |
|---|---|---|---|
| ALKYLAMINE | pending | **8** | "needs a chain re-run, not a data fix" |
| CREDITACC | verified | 4 | re-run from scratch on the ADR-0096 fact base |
| FIVESTAR | pending | 2 | packet ready, 7 writers not run |
| GAYATRI | pending | 1 | packet ready, 7 writers not run |
| PCJEWELLER | verified | 4 | re-run after A38 moved the checklist |
| SYMPHONY | pending | 1 | packet ready, 7 writers not run |

ALKYLAMINE sits at 8 attempts against an escalation rule that blocks at 3. FIVESTAR's failure is four
computed metrics in the report the compute layer does not produce, plus a narrative absence claim the
fact base contradicts — i.e. a Law 1 violation that reached the checker instead of being stopped
earlier.

### 1.4 The rework killer is built and unplugged

`verify/precheck_answers.py` (111 lines) exists and is unit-tested
(`tests/test_verify_precheck_answers.py`). Its docstring shows manual invocation:

```
python3 verify/precheck_answers.py /tmp/pk_PCJEWELLER
```

A grep for `precheck` across `src/` and the loop protocol finds **no caller**. Running it against the
packet *before* the writers run is what stops FIVESTAR-class failures at the packet instead of after
report assembly.

### 1.5 The evidence ledger already exists — it is `--readings`

`firm deep-dive --readings` (ADR-0046/0055) takes verified reading answers as `{stem}.reading.json`,
described in the CLI help as: *"every figure verified against the page text, every period dated."*
That **is** the one-read-many-uses ledger; it does not need building.

The gap is inconsistent invocation:

| unit | invocation | verified? |
|---|---|---|
| PCJEWELLER | `--filings --readings` | yes |
| CREDITACC | `--filings --documents` | yes |
| ALKYLAMINE | `--documents` only | no |

Both verified units used `--filings`. Standardising on `--filings --readings` costs nothing and is
probably the single highest reliability-per-effort change available.

### 1.6 One real blocker for the new doctrine

`config/roster.yaml` lists prerequisite `segments` as **`NOT INGESTED — see A44/A45`**.

Segments are **L2** (disclosed components) for revenue — the most load-bearing link in the chain for a
non-bank. `ANALYSIS_DOCTRINE.md` §2 cannot run at full depth until segments are ingested. This is the
one data dependency that gates the doctrine.

---

## 2. Four changes, ranked by payoff over effort

| # | Change | Effort | Buys |
|---|---|---|---|
| 1 | Fill the three model placeholders in `config/models.yaml` | minutes, config only | Cheap model on extraction/classification; strongest reserved for synthesis/red_team/valuation |
| 2 | `ThreadPoolExecutor` over `deep_dive.py:1309`, keyed by roster `stage` | contained code change | 14 serial calls → 7 stage barriers. Est. ~2–3× wall-clock |
| 3 | Make `--filings --readings` the standard invocation | none | Both verified units used `--filings`; the reading path is the ledger |
| 4 | Call `precheck_answers.py` before writers run | small | Catches Law 1 violations at the packet, not after assembly |

---

## 3. The doctrine only executes if it is in the checker

`CLAUDE.md` is unambiguous: *"Your own judgement does not decide done. Only the exit code does."*
A doctrine `verify/check_report.py` does not test is decorative in that repo.

`ANALYSIS_DOCTRINE.md` was written to be mechanically checkable. These all reduce to assertions:

- 8 links present per chain record, each carrying a declared state (§2b)
- domain count ≥ 3 with ≥ 1 non-statement (§1b)
- S1–S6 present on every finding; S5 and S6 non-empty (§1a)
- no-recommendation regex on S6 (§1c)
- every table followed by the conclusion it supports — the data-print check (§1f)
- every `BROKEN` link reaching the red-flag register (§2c)

That is the difference between the doctrine changing output and sitting unread in `docs/`.

---

## 4. The run sequence

`docs/directives/TRACER_BULLET_DIRECTIVE.md` governs: one thin slice end to end, then widen one
dimension at a time. Not "run all six units."

1. **Config only** — changes #1 and #3. No code, reversible.
2. **Add the §10 interpretation assertions to `verify/check_report.py`.** Checker before analysis, so
   the target is defined by exit code rather than by judgement.
3. **Tracer: SYMPHONY.** Packet ready, writers unrun, and a non-bank — the general doctrine's actual
   subject. One line item → one full L1–L8 chain → one finding through S1–S6 → one QC pass. Reviewed in
   a fresh context per `docs/directives/FRESH_CONTEXT_REVIEW_RULE.md`.
4. **Widen to the full report on that one company.**
5. **Then change #2** (parallelism), with its own fresh-context review — it is the only real code change
   in the list.
6. **Then GAYATRI and FIVESTAR**, whose packets are also ready.

**ALKYLAMINE should be marked `blocked` and left alone.** Its own rule says a fourth attempt has never
once been the fix, and it is at eight. Its recorded error says it needs a chain re-run, not analysis.

---

## 5. What was NOT done

Nothing in `~/Desktop/equity reserch` was modified. Specifically not applied:

- `config/models.yaml` placeholders — untouched
- parallelism over the serial agent loop — untouched
- `verify/check_report.py` assertions — untouched
- `--filings --readings` standardisation — untouched
- `state/progress.json` (ALKYLAMINE blocking) — untouched

All of the above are recommendations, measured from a read-only pass.
