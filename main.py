def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    count_words = word_count(book_text)
    # print(book_text)
    print(f"{count_words} words found in the document")

main()

