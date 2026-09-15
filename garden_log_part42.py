# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: GardenLog
import sys

class GardenANSI:
    """ANSI color codes for terminal output with toggle support."""

    _enabled = True

    @classmethod
    def toggle(cls, state: bool):
        cls._enabled = state

    @classmethod
    def enabled(cls) -> bool:
        return cls._enabled

    @classmethod
    def _check(cls):
        if not cls._enabled:
            return
        if sys.stdout.isatty():
            sys.stdout.write(cls._colors[cls._color])
        sys.stdout.write(cls._text)
        if not cls._enabled:
            return
        if sys.stdout.isatty():
            sys.stdout.write(cls._reset)

    _colors = {
        'red':    '\033[31m',
        'green':  '\033[32m',
        'yellow': '\033[33m',
        'blue':   '\033[34m',
        'magenta':'\033[35m',
        'cyan':   '\033[36m',
        'white':  '\033[37m',
        'bold':   '\033[1m',
    }
    _reset = '\033[0m'

    @classmethod
    def print(cls, text: str, color: str = 'green', bold: bool = False):
        cls._text = text
        cls._color = color
        if bold:
            cls._colors[color] = cls._colors['bold'] + cls._colors[color]
        cls._print()

    @classmethod
    def _print(cls):
        if cls._enabled:
            sys.stdout.write(cls._colors[cls._color])
        sys.stdout.write(cls._text)
        if cls._enabled:
            sys.stdout.write(cls._reset)
        sys.stdout.write('\n')
        sys.stdout.flush()

    @classmethod
    def header(cls, text: str):
        cls.print(text, 'cyan', bold=True)

    @classmethod
    def info(cls, text: str):
        cls.print(text, 'blue')

    @classmethod
    def success(cls, text: str):
        cls.print(text, 'green')

    @classmethod
    def warning(cls, text: str):
        cls.print(text, 'yellow')

    @classmethod
    def error(cls, text: str):
        cls.print(text, 'red')
