"""
    - A small program to read and summarize a large text file
"""

def main():
    path = "/home/miles/Documents/Programming/Python/bookbot/books/short.txt"
    file_contents = get_file_text(path)
    print(f"There are {word_count(file_contents)} words!\n")
    
    
    alphabet, digits, special = character_count(file_contents)
    
    print("Alphabet:")
    [print(f"\tThe '{sub_dict['char']}' character was found {sub_dict['num']} times") for sub_dict in alphabet]
    
    print("\nDigits: ")
    [print(f"\tThe '{sub_dict['char']}' character was found {sub_dict['num']} times") for sub_dict in digits]

    print("\nSpecial Chars: ")
    for sub_dict in special:
        char = sub_dict['char']
        if char == '\t': char = "\\t"
        elif char == '\n': char = "\\n"
        print(f"\tThe '{char}' character was found {sub_dict['num']} times")

        
def word_count(contents):
    return len(contents.split())

def get_file_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(contents):
    contents_chars = str(contents)
    alphabet_dict = {}
    number_dict = {}
    character_dict = {}
    
    # get the count for each letter, char, and num differently
    for char in contents_chars:
        char = char.lower()
        
        # check alphabet
        if char in ['a','b','c','d','e','f','g','h','i','j','k','l',
                    'm','n','o','p','q','r','s','t','u','v','w',
                    'x','y','z']:
            if char in alphabet_dict.keys():
                alphabet_dict[char] += 1
            else:
                alphabet_dict[char] = 1
                
        # number
        elif char in ['1','2','3','4','5','6','7','8','9','0']:
            if char in number_dict.keys():
                number_dict[char] += 1
            else:
                number_dict[char] = 1
            
        # special character
        else:
            if char in character_dict.keys():
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    
    
    return sort_dict(alphabet_dict), sort_dict(number_dict), sort_dict(character_dict)

def sort_dict(dictionary):
    # convert into list of dictionaries in the following format
    # dictionary = [
    #  { "char" : key, "num" : value}   
    #]
    new_dict = [{"char" : key, "num" : dictionary[key]} for key in dictionary.keys()]
    new_dict.sort(reverse=True, key=lambda x : x["num"])
    return new_dict

if __name__ == "__main__":
    main()