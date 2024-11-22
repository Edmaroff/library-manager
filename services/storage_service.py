import json
from typing import List

from models.book import Book


class StorageService:
    """Класс для сохранения и загрузки книг из файла JSON"""

    def __init__(
        self,
        data_file: str = "library.json",
    ):
        self.data_file = data_file

    def load_books(self) -> List[Book]:
        """Загрузка списка книг из JSON файла"""

        try:
            with open(
                self.data_file,
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except (
            FileNotFoundError,
            json.JSONDecodeError,
        ):
            return []

    def save_books(self, books: List[Book]):
        """Сохранение списка книг в JSON файл"""

        with open(
            self.data_file,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                [book.to_dict() for book in books],
                file,
                ensure_ascii=False,
                indent=4,
            )
