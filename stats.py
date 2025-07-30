def number_of_words(book_text):
    """Get number of words in a book file.

    :param book_text: str - full text of book
    :return: int - number of total words in the book

    Function that takes the full string of text extracted from a book file, and returns the total number of words in the book file as an integer.
    """

    return len(book_text.split())

def number_of_chars(book_text):
    """Count the number of characters in a book.

    :param book_text: str - full text of book
    :return: dict - dictionary with characters as the key and number of occurences as the value

    Function that takes the full text of a book and returns a dictionary containing each character and the number of times each character occurs in the book.
    """

    pass
