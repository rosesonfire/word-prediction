from src.config import FILE_NAME
from src.utils.db import db
from src.utils.string import clean_word

with open(FILE_NAME, "r", encoding="utf-8") as f:
    for line in f:
        sentences = line.split(".")

        for sentence in sentences:
            words = sentence.split()

            if not words:
                continue

            prev_word = clean_word(words[0])

            if not prev_word:
                continue

            for word in words[1:]:
                word = clean_word(word)

                if not word:
                    continue

                # Use priority queue to store the next word index.
                # Increase the current recorded frequency
                # of `prev_word -> word` by 1.
                db.zincrby(prev_word, 1, word)

                prev_word = word
