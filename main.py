def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of " + str(book_path) + " ---")
    print(f"{num_words} words found in the document\n")
    print_report(text)

    print("--- End report ---")
     

def print_report(text):
    strings_dict = get_num_strings(text)
    sorted_list = []
    for ch in strings_dict:
        sorted_list.append({"char": ch, "num": strings_dict[ch]})

    # Sort the list
    sorted_list.sort(reverse=True, key=lambda item: item['num'])

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        # Use the correct key 'num' instead of 'count'
        print(f"The '{item['char']}' character was found {item['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_strings(text):
    strings_dict = {}
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    text = text.lower()
    for char in text:  # Iterate over each character
        if char in alphabet:  # Check if the character is in the alphabet
            if char in strings_dict:
                strings_dict[char] += 1  # Increment count if character exists
            else:
                strings_dict[char] = 1  # Initialize count if character does not exist
    return strings_dict


main()