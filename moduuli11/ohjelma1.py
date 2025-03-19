#!/usr/bin/env python3

# Muutin nimet englanniksi, ei kai haittaa

class Publication:
    def __init__(self, name):
        self.name = name



class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_details(self):
        print(f"{self.name}, {self.author}, {self.pages}")



class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_details(self):
        print(f"{self.name}, {self.editor}")


class Article(Publication):
    pass



def main():
    book = Book("Hytti n:o 6", "Rosa Liksom", 200)
    book.print_details()

    mag = Magazine("Aku Ankka", "Aki Hyyppä")
    mag.print_details()

if __name__ == "__main__":
    main()
