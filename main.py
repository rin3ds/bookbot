import sys

from stats import get_book_text, get_num_words, count_characters

book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)
    
    char_stats = count_characters(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in char_stats:
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
