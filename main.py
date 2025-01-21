import string

def count_characters(text: str):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    lower_text = text.lower()
    for c in lower_text:
        if c in string.ascii_lowercase:
            letter_count[c] += 1
    return letter_count

with open("./books/frankenstein.txt") as f:
    frankenstein_txt = f.read()
    count = count_characters(frankenstein_txt)
    print(count)
    f.close()

