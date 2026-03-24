import re

from more_itertools import sliding_window

from src.config import FILE_NAME
from src.utils.db import db
from src.utils.string import clean_word


class Indexer:
    def __init__(self):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                sentences = re.split(r'[.,?;:!…—"\']', line)

                for sentence in sentences:
                    words = sentence.replace("’", "'").split()
                    words = [clean_word(w) for w in words]
                    words = [w for w in words if w]

                    if not words:
                        continue

                    self._index_1_to_1_sliding_window(words)
                    self._index_1_to_2_sliding_window(words)

    def _index_1_to_1_sliding_window(self, words: list[str]):
        for word, next_word in sliding_window(words, 2):
            db.zincrby(word, 1, next_word)

    def _index_1_to_2_sliding_window(self, words: list[str]):
        for word, next_word, next_next_word in sliding_window(words, 3):
            db.zincrby(word, 1, f"{next_word}:{next_next_word}")

    def get_next_words(self, word: str, position: int) -> list[str] | None:
        next_words = db.zget(word, position)

        return next_words.split(":") if next_words else None
