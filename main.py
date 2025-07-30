from stats import number_of_words

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    num_words = number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()