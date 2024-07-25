"""
    - A small program to read and summarize a large text file
"""

def main():
    with open("/home/miles/Documents/Programming/Python/bookbot/books/short.txt") as f:
        file_contents = f.read()
            
        print(f"There are {word_count(file_contents)} words!")
        
def word_count(contents):
    return len(contents.split())
    

if __name__ == "__main__":
    main()