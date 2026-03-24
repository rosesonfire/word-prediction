# Given a single word W, this prints the probable word sequence that can come
# after W

from src.utils.string import clean_word

from .indexer import Indexer

indexer = Indexer()

next_word_sequence_size = 10

while True:
    word = input(
        f"Type '-' to update the predicted next word sequence size "
        f"[{next_word_sequence_size}]\nSearch: "
    ).strip()

    if word == "-":
        try:
            new_next_word_sequence_size = int(
                input(
                    f"Predicted next word sequence size"
                    f"[{next_word_sequence_size}]: "
                )
            )
        except ValueError:
            print("Could not process input!")

            continue

        if new_next_word_sequence_size < 1:
            print("Predicted next word sequence size cannot be less than 1")

            continue

        next_word_sequence_size = new_next_word_sequence_size

        continue

    word = clean_word(word)

    if not word:
        continue

    sequence = [word]
    word_counts = {}

    for _ in range(next_word_sequence_size):
        # Get the most frequent next word from the priority queue for `word`.
        # If the most frequent next word is already used, then use the next most
        # frequent. And so on and so forth until there is no next frequent word
        # left for `word`. Then it resets back to the most frequent next word.
        word_count = word_counts.get(word, 0)
        next_words = indexer.get_next_words(word, word_count)

        if not next_words:
            if word_count > 0:
                word_count = 0

                next_words = indexer.get_next_words(word, word_count)

            # Stop the sequence abruptly if no next word is found for 'word'
            break

        sequence.extend(next_words)

        word_counts[word] = word_count + 1
        word = next_words[-1]

    print(" ".join(sequence))
