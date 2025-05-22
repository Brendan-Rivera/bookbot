def get_word_count(book):
    word_list = book.split()
    counter = -1
    for word in word_list:
        counter += 1
    
    return f"Found {counter} total words"

def get_count_characters(book):
    book_to_split = book.lower()
    chars = [c for c in book_to_split]
    new_dict = dict()

    for char in chars:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
    
    return new_dict

def split_sort_dictionary(dictionary):
    new_list = []

    for key, value in dictionary.items():
        new_list.append({"char" : key, "num" : value})
 
    new_list.sort(reverse=True, key=lambda x : x["num"])

    return new_list