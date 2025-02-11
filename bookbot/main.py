def count_words(book: str) -> dict:
    dict_characters={}
    for character in book:

        char = character.lower()
        if char in dict_characters.keys():
            dict_characters[char] += 1
        else:
            dict_characters[char] = 1
    return dict_characters

def check_alpha_n_sort(dict) -> list:
    sorted_list = []
    keys_list = []
    for key,item in dict.items():
        if key.isalpha():
            sorted_list.append(item)
            keys_list.append(key)

    zip_lists = zip(sorted_list, keys_list)
    zip_lists_sorted = sorted(zip_lists, reverse=True)

    return zip_lists_sorted 

def summary(book: str):
    character_dictionary = count_words(book)
    zip_lists_sorted = check_alpha_n_sort(character_dictionary)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(book.split())} words found in this document')

    for number, key in zip_lists_sorted :
        print(f"The '{key}' character was found {number} times")

    return


def main() -> int:

    '''executes the code and returns exit code 0'''

    path_to_file =  "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        summary(file_contents)        
    return 0

if __name__ == '__main__':
    main()
