import re


def clean_word(word: str) -> str | None:
    # Intended to remove punctuations, except apostrophes
    return re.sub(r"[^a-zA-Z']", "", word) or None
