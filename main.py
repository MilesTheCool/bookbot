"""
    - A small program to read and summarize a large text file
"""

def main():
    path = "/home/miles/Documents/Programming/Python/bookbot/books/short.txt"
    file_contents = get_file_text(path)
    print(f"There are {word_count(file_contents)} words!")
    
    print("\n\nCharacter Count: ", character_count(file_contents)) 
    
def word_count(contents):
    return len(contents.split())

def get_file_text(path):
    with open(path) as f:
        return f.read()
    
def character_count(contents):
    contents_chars = str(contents)
    contents_dict = {}

    for char in contents_chars:
        if char in contents_dict.keys():
            contents_dict[char] += 1
        else:
            contents_dict[char] = 1
    
    return contents_dict

if __name__ == "__main__":
    main()