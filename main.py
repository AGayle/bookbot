import sys
from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")   
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        text = get_book_text(book_path)
        word_count = get_word_count(text)
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        char_dict = get_char_count(text)
        sorted_list = get_sorted_list(char_dict)
        for dict in sorted_list:
            if(dict['char'].isalpha()):
                print(f"{dict['char']}: {dict['num']}")
        print("============= END ===============")
        sys.exit(0)
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()