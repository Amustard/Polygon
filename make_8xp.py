"""Tokenize a program listing (e.g. POLYGON.txt) into a TI-83 Plus / TI-84 Plus .8xp file.

Only the tokens this program uses are in the table.
Usage: python3 make_8xp.py [POLYGON.txt] [POLYGON.8xp]
The on-calculator program name is taken from the output file name.
"""
import os
import sys

# Multi-character tokens. A trailing space is part of the token where the
# calculator itself shows one (e.g. "Lbl ", "If ").
WORDS = {
    "Degree": b"\x65", "Float": b"\x69",
    "Lbl ": b"\xD6", "Goto ": b"\xD7", "If ": b"\xCE", "Then": b"\xCF",
    "End": b"\xD4", "For(": b"\xD3", "Pause ": b"\xD8", "Input ": b"\xDC",
    "Disp ": b"\xDE", "Output(": b"\xE0", "ClrHome": b"\xE1", "Menu(": b"\xE6",
    "PlotsOff ": b"\xEA", "FnOff ": b"\x97", "ClrDraw": b"\x85",
    "ZSquare": b"\x8B", "Text(": b"\x93", "Line(": b"\x9C",
    "round(": b"\x12", "abs(": b"\xB2", "fPart(": b"\xBA", "√(": b"\xBC",
    "sin(": b"\xC2", "cos(": b"\xC4", "tan(": b"\xC6", "Else": b"\xD0", " or ": b"\x3C", " and ": b"\x40",
    "AxesOff": b"\x7E\x09", "GridOff": b"\x7E\x0B", "LabelOff": b"\x7E\x0D",
    "Xmin": b"\x63\x0A", "Xmax": b"\x63\x0B", "Ymin": b"\x63\x0C",
    "Ymax": b"\x63\x0D", "Str1": b"\xAA\x00",
}

CHARS = {
    " ": b"\x29", '"': b"\x2A", ",": b"\x2B", ".": b"\x3A", ":": b"\x3E",
    "?": b"\xAF", "!": b"\x2D", "(": b"\x10", ")": b"\x11", "=": b"\x6A",
    "<": b"\x6B", ">": b"\x6C", "≤": b"\x6D", "≥": b"\x6E", "+": b"\x70",
    "-": b"\x71", "*": b"\x82", "/": b"\x83", "→": b"\x04", "⁻": b"\xB0",
}
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    CHARS[c] = bytes([ord(c)])
for c in "0123456789":
    CHARS[c] = bytes([0x30 + int(c)])

WORD_KEYS = sorted(WORDS, key=len, reverse=True)


def tokenize_line(line, lineno):
    out, i, in_str = bytearray(), 0, False
    while i < len(line):
        if line[i] == '"':
            in_str = not in_str
            out += CHARS['"']
            i += 1
            continue
        if not in_str:
            for w in WORD_KEYS:
                # a token's trailing space may be missing at the end of a line
                if line.startswith(w, i) or (w.endswith(" ") and line[i:] == w[:-1]):
                    out += WORDS[w]
                    i += len(w)
                    break
            else:
                ch = line[i]
                if ch == " ":
                    raise SyntaxError(f"line {lineno}: stray space outside a string")
                if ch not in CHARS:
                    raise SyntaxError(f"line {lineno}: unknown character {ch!r}")
                out += CHARS[ch]
                i += 1
        else:
            ch = line[i]
            if ch not in CHARS:
                raise SyntaxError(f"line {lineno}: character {ch!r} not allowed in string")
            out += CHARS[ch]
            i += 1
    if in_str:
        raise SyntaxError(f"line {lineno}: unclosed string")
    return bytes(out)


def build_8xp(name, tokens, comment):
    data = len(tokens).to_bytes(2, "little") + tokens
    entry = (b"\x0D\x00" + len(data).to_bytes(2, "little") + b"\x05"
             + name.encode().ljust(8, b"\0") + b"\x00\x00"
             + len(data).to_bytes(2, "little") + data)
    comment = comment.encode()[:42].ljust(42, b"\0")
    header = b"**TI83F*\x1A\x0A\x00" + comment + len(entry).to_bytes(2, "little")
    return header + entry + (sum(entry) & 0xFFFF).to_bytes(2, "little")


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "POLYGON.txt"
    dst = sys.argv[2] if len(sys.argv) > 2 else "POLYGON.8xp"
    lines = open(src, encoding="utf-8").read().rstrip("\n").split("\n")
    tokens = b"\x3F".join(tokenize_line(l, n + 1) for n, l in enumerate(lines))
    name = os.path.splitext(os.path.basename(dst))[0].upper()[:8]
    open(dst, "wb").write(build_8xp(name, tokens, f"{name} program"))
    print(f"wrote {dst}: {len(lines)} lines, {len(tokens)} token bytes")


if __name__ == "__main__":
    main()
