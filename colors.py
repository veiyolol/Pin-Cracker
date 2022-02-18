# One function to change RGB values to an ASNI expression.
def get_ansi_color(r, g, b, text) -> str:
  # .format is faster B')
  return """\033[38;2;{};{};{}m{}\033[38;2;255;255;255m""".format(r, g, b, text)
