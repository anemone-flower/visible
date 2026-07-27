# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GardenLog
def print_table(title, headers, rows):
    """Compact table printer: draws a console table with borders."""
    if not headers or not rows:
        print(f"\n{title}\n")
        return
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            w = len(str(val)) if val is not None else 0
            col_widths[i] = max(col_widths[i], w)
    col_widths = [max(w, 3) for w in col_widths]
    header_line = "│" + "┌───".join(["-" * (w + 2) for w in col_widths]) + "┐"
    sep_line   = "│" + "─┼─".join(["-" * (w + 2) for w in col_widths]) + "┘"
    body_line  = "│" + "─┤".join(["-" * (w + 2) for w in col_widths]) + "└"
    print(f"\n{title}")
    print(header_line)
    print(sep_line)
    for row in rows:
        line = "│"
        for i, val in enumerate(row):
            cell = str(val)[:col_widths[i]] if val is not None else ""
            pad = col_widths[i] - len(cell)
            line += f" {cell:<{pad}} │"
        print(line.rstrip())
    print(sep_line)
