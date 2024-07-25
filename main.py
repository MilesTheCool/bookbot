"""
    - A small program to read and summarize a large text file
"""

def main():
    with open("/home/miles/Documents/Programming/Python/bookbot/books/short.txt") as f:
        file_contents = f.read()
            
        print(file_contents)

if __name__ == "__main__":
    main()