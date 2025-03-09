from stats import word_count
from stats import character_count
from stats import sort_counts

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    count_words = word_count(book_text)
    char_count = character_count(book_text)
    sortedcounts = sort_counts(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")

    for i in sortedcounts:
        print(f"{i['char']}: {i['count']}")
    print("============= END ===============")
    

main()

