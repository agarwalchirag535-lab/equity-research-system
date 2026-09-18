"""
Shared styling + helpers for the BSE model builder.
Formatting rules (strict):
  - Blue font (0,0,255)  -> hardcoded inputs / assumptions / typed historical actuals
  - Black font           -> formula referencing only the SAME sheet
  - Green font (0,128,0)  -> formula referencing ANOTHER sheet
  - Yellow fill          -> every editable assumption cell
  - Rs Crore throughout; thousands separator; negatives in parentheses; zero as "-"
  - Percentages stored as decimals; rendered with 1 dp
  - Years as text
"""
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, NamedStyle
from openpyxl.comments import Comment

# ---- colours ----
BLUE = "FF0000FF"
BLACK = "FF000000"
GREEN = "FF008000"
WHITE = "FFFFFFFF"
HDR_BG = "FF1F3864"      # dark blue header
SUBHDR_BG = "FFD9E1F2"   # light blue section header
YELLOW = "FFFFFF00"      # editable assumption fill
GREY = "FFF2F2F2"

# ---- number formats ----
FMT_CR = '#,##0.0;(#,##0.0);"-"'          # Rs crore, 1 dp, parens neg, dash zero
FMT_CR0 = '#,##0;(#,##0);"-"'             # Rs crore, 0 dp
FMT_PCT = '0.0%;(0.0%);"-"'               # percentage from decimal
FMT_BPS = '#,##0.00"  bps";(#,##0.00);"-"'
FMT_X = '#,##0.0"x";(#,##0.0"x");"-"'     # multiple
FMT_RS = '#,##0.00;(#,##0.00);"-"'         # rupees (per share)
FMT_NUM = '#,##0.00;(#,##0.00);"-"'
FMT_YR = '@'                               # text

THIN = Side(style="thin", color="FFBFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
TOPBORDER = Border(top=Side(style="thin", color="FF000000"))
DBLTOP = Border(top=Side(style="double", color="FF000000"))


def font_for(formula: str, cross_sheet: bool = None, bold=False):
    """Return the correct font for a value/formula string."""
    if isinstance(formula, str) and formula.startswith("="):
        is_cross = ("!" in formula) if cross_sheet is None else cross_sheet
        return Font(name="Calibri", size=10, color=(GREEN if is_cross else BLACK), bold=bold)
    # a typed value -> blue input
    return Font(name="Calibri", size=10, color=BLUE, bold=bold)


def set_cell(ws, coord, value, *, fmt=None, input_cell=False, bold=False,
             cross=None, align="right", comment=None, force_color=None):
    """Write a cell applying the formatting doctrine automatically.
    - input_cell=True forces blue font + yellow fill (an editable assumption).
    - otherwise font is chosen by whether value is a cross-sheet formula.
    """
    c = ws[coord]
    c.value = value
    if force_color:
        c.font = Font(name="Calibri", size=10, color=force_color, bold=bold)
    elif input_cell:
        c.font = Font(name="Calibri", size=10, color=BLUE, bold=bold)
    else:
        c.font = font_for(value, cross_sheet=cross, bold=bold)
    if input_cell:
        c.fill = PatternFill("solid", fgColor=YELLOW)
    if fmt:
        c.number_format = fmt
    c.alignment = Alignment(horizontal=align, vertical="center")
    if comment:
        cm = Comment(comment, "BSE model")
        cm.width = 340
        cm.height = 160
        c.comment = cm
    return c


def label(ws, coord, text, *, bold=False, indent=0, italic=False, size=10, color=BLACK):
    c = ws[coord]
    # a leading '=' would be parsed as a formula; labels are always text.
    if isinstance(text, str) and text.startswith("="):
        text = " " + text
    c.value = text
    c.font = Font(name="Calibri", size=size, bold=bold, italic=italic, color=color)
    c.alignment = Alignment(horizontal="left", vertical="center", indent=indent)
    return c


def section(ws, row, text, span_end_col):
    """Light-blue section header bar across columns A..span_end_col."""
    from openpyxl.utils import get_column_letter
    c = ws.cell(row=row, column=1)
    c.value = text
    c.font = Font(name="Calibri", size=10, bold=True, color="FF1F3864")
    for col in range(1, span_end_col + 1):
        cc = ws.cell(row=row, column=col)
        cc.fill = PatternFill("solid", fgColor=SUBHDR_BG)
    ws.cell(row=row, column=1).alignment = Alignment(horizontal="left", vertical="center")


def title_block(ws, title, subtitle, unit_note, ncols):
    from openpyxl.utils import get_column_letter
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    t = ws.cell(row=1, column=1)
    t.value = title
    t.font = Font(name="Calibri", size=14, bold=True, color=WHITE)
    t.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    for col in range(1, ncols + 1):
        ws.cell(row=1, column=col).fill = PatternFill("solid", fgColor=HDR_BG)
    ws.row_dimensions[1].height = 24

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    s = ws.cell(row=2, column=1)
    s.value = subtitle
    s.font = Font(name="Calibri", size=9, italic=True, color="FF444444")
    s.alignment = Alignment(horizontal="left", vertical="center", indent=1)

    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=ncols)
    u = ws.cell(row=3, column=1)
    u.value = unit_note
    u.font = Font(name="Calibri", size=9, bold=True, color="FFC00000")
    u.alignment = Alignment(horizontal="left", vertical="center", indent=1)


def year_header(ws, row, first_col, years, *, hist_count=3):
    """Write year headers as TEXT, tint historical vs projected differently."""
    from openpyxl.utils import get_column_letter
    for i, y in enumerate(years):
        col = first_col + i
        c = ws.cell(row=row, column=col)
        c.value = y
        c.number_format = FMT_YR
        c.font = Font(name="Calibri", size=10, bold=True, color=WHITE)
        c.alignment = Alignment(horizontal="center", vertical="center")
        bg = "FF375623" if i >= hist_count else "FF833C00"  # green=hist, brown=proj
        c.fill = PatternFill("solid", fgColor=bg)
    # legend labels
    ws.cell(row=row - 1, column=first_col).value = "Actual"
    ws.cell(row=row - 1, column=first_col).font = Font(size=8, italic=True, color="FF375623")
    ws.cell(row=row - 1, column=first_col + hist_count).value = "Projected"
    ws.cell(row=row - 1, column=first_col + hist_count).font = Font(size=8, italic=True, color="FF833C00")
