import copy
import re
from enum import Enum


class Colors(Enum):
    # ANSI color codes
    # https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[33m'


class CssColors(Enum):
    BLUE = 'blue'
    CYAN = 'cyan'
    GREEN = 'green'
    RED = 'red'
    YELLOW = 'yellow'


def emphasize_span(line, span=None, capitalize=True, underline=False, color=Colors.BLUE, css=False):
    if isinstance(span, list):
        matches = copy.deepcopy(span)
    elif isinstance(span, tuple):
        matches = [span]
    else:  # span is None, highlight the whole line
        matches = [(0, len(line))]
    if not isinstance(color, list):
        color = [color]
    if css:
        if any(isinstance(c, Colors) for c in color):
            raise ValueError(f"in css mode color should be an instance of CssColors")
        color = [f"<span style=\"color: {c.value};\">" for c in color]
    else:
        color = [c.value for c in color]

    for i, m in enumerate(sorted(matches, key=lambda x: x[0], reverse=True)):
        c = color[min(len(color) - 1, i)]
        line = _emphasize(line, m, capitalize=capitalize, underline=underline, color=c, css=css)
    return line


def emphasize_wrd(line, wrd=None, capitalize=True, underline=False, color=Colors.BLUE, re_escape=False, flags=re.I, return_matches=False, css=False):
    if isinstance(wrd, str):
        wrd = [wrd]
    if isinstance(wrd, list):
        matches = []
        for w in set(wrd):
            matches.extend([m.span() for m in re.finditer(rf"{re.escape(w) if re_escape else w}", line, flags=flags)])
    else:  # wrd is None, highlight the whole line
        matches = [(0, len(line))]
    if not isinstance(color, list):
        color = [color]
    if css:
        if any(isinstance(c, Colors) for c in color):
            raise ValueError(f"in css mode color should be an instance of CssColors")
        color = [f"<span style=\"color: {c.value};\">" for c in color]
    else:
        color = [c.value for c in color]

    for i, m in enumerate(sorted(matches, key=lambda x: x[0], reverse=True)):
        c = color[i % len(color)]
        line = _emphasize(line, m, capitalize=capitalize, underline=underline, color=c, css=css)
    if return_matches:
        return line, matches
    return line


def _emphasize(line, span, capitalize=True, underline=True, color: Colors = None, css=False):
    underline_beg = "\033[4m"
    if css:
        style_end = "</span>"
    else:
        style_end = "\033[0m"
    bold = '\033[1m'  # TODO: Implement
    if capitalize:
        line = line[:span[0]] + line[span[0]: span[1]].upper() + line[span[1]:]
    if underline:
        line = line[:span[1]] + style_end + line[span[1]:]
        line = line[:span[0]] + underline_beg + line[span[0]:]
        span = tuple((span[0] + len(underline_beg), span[1] + len(style_end)))
    if color:
        line = line[:span[1]] + style_end + line[span[1]:]
        line = line[:span[0]] + color + line[span[0]:]
        # span = tuple((span[0] + len(color), span[1] + len(Colors.END.value)))  # TODO: Enable if we add more emphasis states below

    return line


if __name__ == "__main__":
    word1, word2, word3, word4, word5 = 'she', 'sea', '(sea shore)', '^she', r'\bsea\b'
    arb = "الرح"
    line = 'She sells seashells by the sea shore. She sells seashells by the (sea shore).'
    line2 = 'She sells seashells by the sea shore.\nShe sells seashells by the sea shore.'
    line3 = 'بسم الله الرحمن الرحيم'
    print(emphasize_span(line, [(0, 5), (10, 17)], color=Colors.GREEN))  # by span
    print(emphasize_wrd(line, word1, color=Colors.BLUE))  # by word
    print(emphasize_wrd(line, word3, color=Colors.RED, re_escape=True))  # to catch parentheses
    print(emphasize_wrd(line, [word1, word2], color=Colors.BLUE))  # list of words
    print(emphasize_wrd(line, [word1, word2], color=[Colors.BLUE, Colors.GREEN]))  # list of words, alternating colors
    print(emphasize_wrd(line, None, color=Colors.BLUE))  # whole line
    print(emphasize_wrd(line2, word4, capitalize=False, color=Colors.CYAN, flags=re.I|re.M))  # only beginning of line
    print(emphasize_wrd(line, word5, capitalize=False, color=Colors.CYAN, flags=re.I|re.M))  # only whole word
    print(emphasize_wrd(line3, arb, capitalize=False, color=Colors.CYAN))  # arabic
