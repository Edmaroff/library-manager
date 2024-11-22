<img src="https://img.shields.io/badge/python-3.12-blue" alt="Python version"/> <img src="https://img.shields.io/badge/Pytest-8.3.3-blue" alt="Pytest Version"/>
<h1>Library Manager</h1>

<h2>Описание</h2>
<p>
    <strong>Library Manager</strong> — это консольное приложение для управления библиотекой книг. 
    Позволяет добавлять, удалять, искать и отображать книги, а также изменять их статус.
</p>

<h2>Функционал</h2>
<ul>
    <li><strong>Добавление книги:</strong> Введите название, автора и год издания.</li>
    <li><strong>Удаление книги:</strong> Удаление книги по ID.</li>
    <li><strong>Поиск книг:</strong> Поиск по названию, автору или году издания.</li>
    <li><strong>Отображение книг:</strong> Показ всех книг с их данными.</li>
    <li><strong>Изменение статуса:</strong> Установка статуса <code>"в наличии"</code> или <code>"выдана"</code>.</li>
</ul>

<h2>Структура проекта</h2>
<ul>
    <li><code>main.py</code> — Точка входа в приложение.</li>
    <li><code>models/</code> — Модели данных (<code>Book</code>).</li>
    <li><code>controllers/</code> — Управление логикой приложения (<code>Library</code>).</li>
    <li><code>views/</code> — Интерфейс командной строки (<code>CLI</code>).</li>
    <li><code>services/</code> — Работа с файлами (<code>StorageService</code>).</li>
    <li><code>tests/</code> — Тесты.</li>
</ul>

<details>
  <summary style="font-size: 1.3em;"><b>Структура библиотеки</b></summary>
  <p>Пример файла библиотеки: <code>library_example.json</code></p>
  <pre>
[
    {
        "id": 1,
        "title": "Начинаем программировать на Python",
        "author": "Тони Гэддис",
        "year": 2024,
        "status": "выдана"
    },
    {
        "id": 2,
        "title": "Изучаем Python",
        "author": "Марк Лутц",
        "year": 2020,
        "status": "в наличии"
    }
]
  </pre>
</details>

<h2>Установка</h2>
<ol>
    <li>Клонируйте репозиторий:
        <pre><code>git clone https://github.com/Edmaroff/library-manager</code></pre>
    </li>
    <li>Перейдите в директорию проекта:
        <pre><code>cd library-manager</code></pre>
    </li>
    <li>Установите и активируйте виртуальное окружение для проекта <code>venv</code>:
        <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
    </li>
    <li>Установите зависимости из <code>requirements.txt</code>:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Запустите приложение:
        <pre><code>python main.py</code></pre>
        <p>Результаты сохраняются в файле <code>library.json</code>.</p>
    </li>
</ol>

<h2>Запуск тестов</h2>
<p>Для запуска тестов выполните команду:</p>
<pre><code>pytest</code></pre>
