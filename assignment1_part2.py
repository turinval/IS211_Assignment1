class Book:
    # Class attributes initialized to blank strings
    author = ""
    title = ""

    def __init__(self, author="", title=""):
        # Instance attributes initialized to the passed arguments
        self.author = author
        self.title = title

    def display(self):
        # Prints the formatted string representing the book
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    # Instantiate the two book objects
    book1 = Book(author="J. K. Rowling", title="Harry Potter and the Goblet of Fire")
    book2 = Book(author="Walter Scott", title="Ivanhoe: A Romance")

    # Call the display method for both objects
    book1.display()
    book2.display()
