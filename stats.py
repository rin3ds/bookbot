book_path = "./books/frankenstein.txt"

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
