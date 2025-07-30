from stats import number_of_words
from stats import number_of_chars

def get_book_text(file_path):
    """Get contents of book file in .txt format.

    :param file_path: str - relative path to .txt book file
    :return: str - full text of the book file

    Function that takes the file path to the .txt book file, reads the file, and then returns its full contents.
    """
    
    with open(file_path) as f:
        return f.read()

def main():

    book_text = get_book_text("books/frankenstein.txt")

    num_words = number_of_words(book_text)

    num_chars = number_of_chars(book_text)

    print(f"{num_words} words found in the document")
    print(num_chars)

main()