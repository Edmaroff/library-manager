from controllers.library_controller import Library


class CLI:
    """Интерфейс командной строки для управления библиотекой."""

    def __init__(self, library: Library):
        self.library = library
        self.menu_actions = {
            "1": self.add_book,
            "2": self.delete_book,
            "3": self.search_books,
            "4": self.display_books,
            "5": self.update_book_status,
            "6": self.exit_program,
        }

    def run(self):
        """Запуск интерфейса командной строки"""

        while True:
            self.display_menu()
            choice = input("Выберите действие: ").strip()
            action = self.menu_actions.get(choice)
            if action:
                try:
                    action()  # Выполнение выбранного действия
                except ValueError as e:
                    print(f"Ошибка: {e}")
                except Exception as e:
                    print(f"Неожиданная ошибка: {e}")
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    @staticmethod
    def display_menu():
        """Вывод меню действий"""

        print("\n--- Библиотека ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

    def add_book(self):
        """Добавить книгу в библиотеку"""

        title = input("Введите название книги: ").strip()
        while not title:
            print("Ошибка: название книги не может быть пустым.")
            title = input("Введите название книги: ").strip()

        author = input("Введите автора книги: ").strip()
        while not author:
            print("Ошибка: автор книги не может быть пустым.")
            author = input("Введите автора книги: ").strip()

        year = self.validate_int_input("Введите год издания книги: ")
        self.library.add_book(title, author, year)
        print("Книга успешно добавлена")

    def delete_book(self):
        """Удалить книгу из библиотеки"""

        book_id = self.validate_int_input("Введите ID книги для удаления: ")
        if self.library.delete_book(book_id):
            print("Книга успешно удалена")
        else:
            print("Книга с таким ID не найдена")

    def search_books(self):
        """Искать книги в библиотеке"""

        while True:  # Цикл для повторного ввода поля поиска
            field = input("По какому полю искать (title/author/year): ").strip().lower()
            if field in ["title", "author", "year"]:
                break  # Выходим из цикла, если поле корректно
            else:
                print(
                    "Ошибка: Неверное поле для поиска. Введите 'title', 'author', или 'year'"
                )

        query = input("Введите значение для поиска: ").strip()
        results = self.library.search_books(query, field)
        if results:
            print("\nНайденные книги:")
            for book in results:
                print(
                    f"{book.id}: {book.title} - {book.author} ({book.year}) [{book.status}]"
                )
        else:
            print("Книги не найдены")

    def display_books(self):
        """Показать все книги в библиотеке."""
        books = self.library.display_books()
        if books:
            print("\nСписок книг:")
            for book in books:
                print(
                    f"{book.id}: {book.title} - {book.author} ({book.year}) [{book.status}]"
                )
        else:
            print("Библиотека пуста")

    def update_book_status(self):
        """Изменить статус книги."""
        book_id = self.validate_int_input("Введите ID книги для изменения статуса: ")
        while True:
            status = input("Введите новый статус (в наличии/выдана): ").strip().lower()
            if status in ["в наличии", "выдана"]:
                if self.library.update_status(book_id, status):
                    print(
                        f"Книга с ID {book_id} успешно обновлена до статуса '{status}'"
                    )
                else:
                    print("Книга с таким ID не найдена")
                break
            else:
                print("Ошибка: Неверный статус. Введите 'в наличии' или 'выдана'")

    def exit_program(self):
        """Завершить работу программы"""

        print("Пока!")
        exit()

    @staticmethod
    def validate_int_input(prompt):
        """Запрашивает у пользователя целое число и проверяет корректность ввода"""

        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("Ошибка: введите корректное число.")
