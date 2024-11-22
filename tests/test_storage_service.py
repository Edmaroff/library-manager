import os

import pytest

from models.book import Book
from services.storage_service import StorageService


@pytest.fixture
def storage_service():
    """Фикстура StorageService с тестовым файлом"""

    file_name = "test_storage.json"
    storage = StorageService(file_name)
    yield storage

    if os.path.exists(file_name):
        os.remove(file_name)


def test_save_and_load_books(storage_service):
    """Тест сохранения и загрузки книг"""

    books = [
        Book(1, "Изучаем Python", "Марк Лутц", 2020, "в наличии"),
        Book(2, "Начинаем программировать на Python", "Тони Гэддис", 2024, "выдана"),
    ]
    storage_service.save_books(books)
    loaded_books = storage_service.load_books()

    assert len(loaded_books) == 2
    assert loaded_books[0].title == "Изучаем Python"
    assert loaded_books[1].status == "выдана"
