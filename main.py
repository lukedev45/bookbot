def get_book_text(path_to_file):
    with open(path_to_file) as book:
        book_contents = book.read()
    return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
