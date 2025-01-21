import string

PATH_TO_BOOK = "books/frankenstein.txt"

def count_characters(text: str):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    lower_text = text.lower()
    for c in lower_text:
        if c in string.ascii_lowercase:
            letter_count[c] += 1
    return letter_count

def generate_report(file: str, num_words: int, char_counts: dict):
    print(f"--- Begin report of {file} ---")
    print(f"{num_words} words found in the document\n\n")
    for c in char_counts.keys():
        print(f"The '{c}' character was found {char_counts[c]} times")

with open(PATH_TO_BOOK) as f:
    frankenstein_txt = f.read()
    count_of_words = len(frankenstein_txt.split())
    count_by_char = count_characters(frankenstein_txt)
    generate_report(PATH_TO_BOOK, count_of_words, count_by_char)
    f.close()

