from typing import List

from models.book import Book
from services.storage_service import StorageService


class Library:
    """Управление библиотекой книг"""

    def __init__(
        self,
        storage_service: StorageService,
    ):
        self.storage = storage_service
        self.books = self.storage.load_books()

    def add_book(
        self,
        title: str,
        author: str,
        year: int,
    ):
        """Добавление новой книги в библиотеку"""

        new_id = (
            max(
                (book.id for book in self.books),
                default=0,
            )
            + 1
        )
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.storage.save_books(self.books)

    def delete_book(self, book_id: int) -> bool:
        """Удаление книги из библиотеки по ID"""

        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.storage.save_books(self.books)
                return True
        return False

    def search_books(self, query: str, field: str) -> List[Book]:
        """Поиск книг по указанному полю (название, автор или год)"""

        if field not in [
            "title",
            "author",
            "year",
        ]:
            raise ValueError(
                "Неверное поле для поиска. Введите 'title', 'author', или 'year'"
            )
        return [
            book
            for book in self.books
            if query.lower() in str(getattr(book, field)).lower()
        ]

    def display_books(
        self,
    ) -> List[Book]:
        """Получение списка всех книг"""

        return self.books

    def update_status(self, book_id: int, status: str) -> bool:
        """Изменение статуса книги"""

        if status not in [
            "в наличии",
            "выдана",
        ]:
            raise ValueError("Неверный статус. Введите 'в наличии' или 'выдана'")
        for book in self.books:
            if book.id == book_id:
                book.status = status
                self.storage.save_books(self.books)
                return True
        return False
