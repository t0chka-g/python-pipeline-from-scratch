# Python pipeline from scratch

Учебный проект, который развивается последовательно от HTTP-запроса к готовой системе. Сейчас реализован только урок 1: программа скачивает HTML главной страницы [Books to Scrape](https://books.toscrape.com/).

Полное объяснение и инструкции для Windows, Linux и macOS: [урок 1 — HTTP и Requests](docs/lessons/01-http-requests.md).

Для быстрого запуска из корня проекта (Linux/macOS):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```

Результат появится в `data/raw/books.html`. Для запуска нужен Python 3 и доступ в интернет.
