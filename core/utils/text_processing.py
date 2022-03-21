import re

from unidecode import unidecode


def clean_text(text: str):
    if text is None:
        return None
    return unidecode(" ".join(text.split()))  # split + join removes spaces with length >1


def normalise_text(text: str):
    if text is None:
        return None
    textWithPuncuationRemoved = re.sub(r"[,.;@#?!&$-_]+", " ", text.lower())
    return clean_text(text=textWithPuncuationRemoved)
