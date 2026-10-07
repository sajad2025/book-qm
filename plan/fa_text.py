"""Helpers for Farsi text in the generated files."""
import re

FA_DIGITS = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

def fa_digits(x):
    return str(x).translate(FA_DIGITS)

# A formula written in plain Latin text inside Farsi prose ("|z+w| <= |z| + |w|")
# is wrapped in a left-to-right isolate (U+2066 ... U+2069), so that the
# right-to-left paragraph does not reorder its symbols.
_RUN = re.compile(r"[A-Za-z0-9|(\[{\\'-](?:[A-Za-z0-9 +\-*/=<>|^_(){}\[\],.:;'!~\\&%]*[A-Za-z0-9)\]}|'^*!])?")

def isolate(text):
    if not text:
        return text
    return _RUN.sub(lambda m: '⁦' + m.group(0) + '⁩', text.replace('⁦', '').replace('⁩', ''))
