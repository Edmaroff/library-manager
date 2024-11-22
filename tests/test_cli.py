import os
from unittest.mock import patch

import pytest

from controllers.library_controller import Library
from models.book import Book
from services.storage_service import StorageService
from views.cli import CLI


@pytest.fixture
def cli_instance():
    """Фикстура для создания CLI с тестовой библиотекой"""

    storage = StorageService("test_cli.json")
    library = Library(storage)
    cli = CLI(library)
    yield cli

    if os.path.exists("test_cli.json"):
        os.remove("test_cli.json")


def test_add_book_cli_calls_library(cli_instance, monkeypatch, capsys):
    """Тест добавления и проверка вызова метода add_book"""

    user_input = iter(["Название", "Автор", "2023"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))

    with patch.object(cli_instance.library, "add_book") as mocked_add_book:
        cli_instance.add_book()
        mocked_add_book.assert_called_once_with("Название", "Автор", 2023)

    captured_output = capsys.readouterr()
    assert "Книга успешно добавлена" in captured_output.out


def test_delete_book_cli_calls_library(cli_instance, monkeypatch, capsys):
    """Тест удаления книги и проверка вызова метода delete_book"""

    cli_instance.library.add_book("Название", "Автор", 2023)
    book_id = cli_instance.library.books[0].id

    user_input = iter([str(book_id)])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))

    with patch.object(cli_instance.library, "delete_book") as mocked_delete_book:
        cli_instance.delete_book()
        mocked_delete_book.assert_called_once_with(book_id)

    captured_output = capsys.readouterr()
    assert "Книга успешно удалена" in captured_output.out


def test_search_books_cli_calls_library(cli_instance, monkeypatch, capsys):
    """Тест поиска книги и проверка вызова метода search_books"""

    user_input = iter(["title", "Название"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))

    with patch.object(cli_instance.library, "search_books") as mocked_search_books:
        cli_instance.search_books()
        mocked_search_books.assert_called_once_with("Название", "title")

    captured_output = capsys.readouterr()
    assert (
        "Найденные книги" in captured_output.out
        or "Книги не найдены" in captured_output.out
    )


def test_display_books_cli_calls_library(cli_instance, capsys):
    """Тест отображения книг  и проверка вызова метода display_books"""

    with patch.object(cli_instance.library, "display_books") as mocked_display_books:
        mocked_display_books.return_value = [
            Book(1, "Название", "Автор", 2023, "в наличии")
        ]
        cli_instance.display_books()
        mocked_display_books.assert_called_once()

    captured_output = capsys.readouterr()
    assert "Список книг" in captured_output.out
    assert "1: Название - Автор (2023) [в наличии]" in captured_output.out


def test_update_book_status_cli_calls_library(cli_instance, monkeypatch, capsys):
    """Тест обновления статуса книги и проверка вызова метода update_status"""

    cli_instance.library.add_book("Название", "Автор", 2023)
    book_id = cli_instance.library.books[0].id

    user_input = iter([str(book_id), "выдана"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))

    with patch.object(cli_instance.library, "update_status") as mocked_update_status:
        cli_instance.update_book_status()
        mocked_update_status.assert_called_once_with(book_id, "выдана")

    captured_output = capsys.readouterr()
    assert f"Книга с ID {book_id} успешно обновлена" in captured_output.out


def test_exit_program(cli_instance, monkeypatch, capsys):
    """Тест завершения работы программы"""

    user_input = iter(["да"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_input))

    with pytest.raises(SystemExit):  # Ожидаем завершение программы
        cli_instance.exit_program()

    captured_output = capsys.readouterr()
    assert "Пока!" in captured_output.out
