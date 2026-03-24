from .config import FILE_NAME, db

# Clear redis
db.flushdb()

with open(FILE_NAME, "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()

        if not words:
            continue

        prev_word = words[0]

        for word in words[1:]:
            # Use priority queue to store the next word index.
            # Increase the current recorded frequency
            # of `prev_word -> word` by 1.
            db.zincrby(prev_word, 1, word)

            prev_word = word

num_of_next_words = 1

while True:
    word = input(
        f"Type '-' to update number of predicted words[{num_of_next_words}]\nSearch: "
    ).strip()

    if not word:
        continue

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

    # Get the most frequent next word from the priority queue
    next_word = db.zrevrange(word, 0, num_of_next_words - 1)

    print(
        ", ".join(next_word)
        if next_word
        else f"'{word}' not found or has no known succeeding word."
    )
