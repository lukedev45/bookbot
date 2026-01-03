import sys
from stats import num_of_words, num_of_characters, sort_characters

def get_book_text(path_to_file):
    with open(path_to_file) as book:
        book_contents = book.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    total_words = num_of_words(text)
    char_counts = num_of_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_chars:
        ch = entry["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")

    print("============= END ===============")

main()
