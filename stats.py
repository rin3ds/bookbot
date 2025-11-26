

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
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts
