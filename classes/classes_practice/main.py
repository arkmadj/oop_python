class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        new_books: list[Book] = []
        for book_item in self.books:
            if book_item.author != book.author or book_item.title != book.title:
                new_books.append(book_item)
        self.books = new_books

    def search_books(self, search_string: str) -> list[Book]:
        result: list[Book] = []
        query = search_string.lower()
        for book in self.books:
            if query in book.author.lower() or query in book.title.lower():
                result.append(book)
        return result
