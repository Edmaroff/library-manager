import os

import pytest

from controllers.library_controller import Library
from services.storage_service import StorageService

TEST_FILE_NAME = "test_library.json"  # Константа для тестового файла


@pytest.fixture(autouse=True)
def cleanup_test_file():
    """Фикстура для удаления файла `test_library.json` перед и после тестов"""
    if os.path.exists(TEST_FILE_NAME):
        os.remove(TEST_FILE_NAME)

    yield  # Выполнение теста

    if os.path.exists(TEST_FILE_NAME):
        os.remove(TEST_FILE_NAME)


@pytest.fixture
def library():
    """Фикстура для создания объекта библиотеки"""

    storage = StorageService(TEST_FILE_NAME)
    library = Library(storage)
    library.books = []
    return library


def test_add_book(library):
    """Тест добавления книги в библиотеку"""

    library.add_book("Название", "Автор", 2021)

    assert len(library.books) == 1
    assert library.books[0].title == "Название"


def test_delete_book(library):
    """Тест удаления книги из библиотеки"""

    library.add_book("Название", "Автор", 2021)
    book_id = library.books[0].id
    result = library.delete_book(book_id)

    assert result is True
    assert len(library.books) == 0


def test_search_books(library):
    """Тест поиска книг в библиотеке"""

    library.add_book(
        "Начинаем программировать на Python",
        "Тони Гэддис",
        2024,
    )
    library.add_book(
        "Изучаем Python",
        "Марк Лутц",
        2020,
    )
    results = library.search_books("Python", "title")

    assert len(results) == 2


def test_update_status(library):
    """Тест обновления статуса книги"""

    library.add_book(
        "Изучаем Python",
        "Марк Лутц",
        2020,
    )
    book_id = library.books[0].id
    library.update_status(book_id, "выдана")

    assert library.books[0].status == "выдана"
