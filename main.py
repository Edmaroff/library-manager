from controllers.library_controller import Library
from services.storage_service import StorageService
from views.cli import CLI


def main():
    """Запуск приложения"""

    storage_service = StorageService()
    library = Library(storage_service)
    cli = CLI(library)
    cli.run()


if __name__ == "__main__":
    main()
