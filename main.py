from stats import get_book_text, get_num_words, count_characters, book_path

def main():
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    char_stats = count_characters(text)
    
    for char, count in sorted(char_stats.items()):
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()
