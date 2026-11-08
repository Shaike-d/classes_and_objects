import classes_for_main_project.class_Book as c


def main():
    books = [c.Book("Clean Code", "Martin", 3),c.Book("Python Basics", "Cohen", 1),]
    books[0].borrow()
    books[1].borrow()
    try:
        books[1].borrow()
    except ValueError as error:
        print("Python Basics ->", error)
    try:
        c.Book("Empty", "Nobody", 0)
    except ValueError as error:
        print("Empty ->", error)
    for book in books:
        print(book, "| available:", book.is_available())
    print("Books in the library:", c.Book.total_books)


if __name__ == "__main__":
    main()