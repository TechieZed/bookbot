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

    Function that takes the full text of a book and returns a dictionary containing each character with the number of times each occurs in the book.
    """

    character_dict = {}

    lower_case = book_text.lower()

    for char in lower_case:
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    
    return character_dict

def generate_sorted_list(character_dict):
    """Generate a sorted list of dictionaries with each character and their count.

    :param character_dict: dict - dictionary with character as key and number of occurences as value
    :return: list - list of dictionaries with char and num keys

    Function that iterates over a dictionary of characters, and sorts them into a list from highest to lowest of each chcarcter and their count.
    """
    sorted_list = []

    def sort_on(items):
        return items["num"]

    for char, num in character_dict.items():
        new_dict = {}
        if char.isalpha():
            new_dict["char"] = char
            new_dict["num"] = num
            sorted_list.append(new_dict)
        
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
