def get_word_count(book_text):
    word_split = book_text.split()
    return len(word_split)

def get_char_count(book_text):
    text = book_text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_sorted_list(unsorted_dict):
    unsorted_list = []
    for key, value in unsorted_dict.items():
        temp_dict = {"char": key, "num": value}
        unsorted_list.append(temp_dict)
    unsorted_list.sort(reverse=True, key=lambda item: item["num"])
    return unsorted_list