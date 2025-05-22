from stats import get_word_count, get_count_characters, split_sort_dictionary
import sys

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{book_path}'")
        sys.exit(1)
    return file_contents


    
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    new_book = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(get_word_count(new_book))
    char_dict = get_count_characters(new_book)
    split_dict = split_sort_dictionary(char_dict)
    print("--------- Character Count -------")
    for item in split_dict:
        if item['char'].isalpha():
            print(f" {item['char']}: {item['num']} ")
    
    print("============= END ===============")
main()