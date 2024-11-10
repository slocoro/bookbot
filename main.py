def main():

    FRANKENSTEIN = "books/frankenstein.txt"

    with open(FRANKENSTEIN, "r") as f:
        text = f.read()
        word_count = get_word_count(text)
        char_count = count_chars(text)

        print(f"Found {word_count} words in book.\n")
        print_char_counts(counts=char_count)


def get_word_count(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict:
    counts = {}
    for char in text:
        char_lowered = char.lower()
        if char_lowered in counts.keys():
            counts[char_lowered] += 1
        else:
            counts[char_lowered] = 1
    return counts


def print_char_counts(counts: dict) -> None:
    for k, v in counts.items():
        if k.isalpha():
            print(f"Letter '{k}' appears {v} times in book.")


if __name__ == "__main__":
    main()
