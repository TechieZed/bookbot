import sys
from stats import number_of_words
from stats import number_of_chars
from stats import generate_sorted_list

def get_book_text(file_path):
    """Get contents of book file in .txt format.

    :param file_path: str - relative path to .txt book file
    :return: str - full text of the book file

    Function that takes the file path to the .txt book file, reads the file, and then returns its full contents.
    """
    
    with open(sys.argv[1]) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    num_words = number_of_words(book_text)

    num_chars = generate_sorted_list(number_of_chars(book_text))

    print(f"Found {num_words} total words")

    for item_dict in num_chars:
        print(f"{item_dict["char"]}: {item_dict["num"]}")

main()