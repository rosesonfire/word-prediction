# Given a single word W, this prints the probable words that can come after W

from src.utils.db import db
from src.utils.string import clean_word

num_of_next_words = 1

while True:
    word = input(
        f"Type '-' to update number of predicted words[{num_of_next_words}]\n"
        f"Search: "
    ).strip()

    if word == "-":
        try:
            new_num_of_next_words = int(
                input(f"number of predicted words[{num_of_next_words}]: ")
            )
        except ValueError:
            print("Could not process input!")

            continue

        if new_num_of_next_words < 1:
            print("Number of predicted words cannot be less than 1")

            continue

        num_of_next_words = new_num_of_next_words

        continue

    word = clean_word(word)

    if not word:
        continue

    # Get the most frequent next words from the priority queue
    next_words = db.zrevrange(word, 0, num_of_next_words - 1)

    print(
        ", ".join(next_words)
        if next_words
        else f"'{word}' not found or has no known succeeding word."
    )
