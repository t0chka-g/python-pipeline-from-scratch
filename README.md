# Python pipeline from scratch

Цель проекта — шаг за шагом научиться создавать Python-приложение и понимать инструменты вокруг него. Каждый урок продолжает один и тот же проект. Сейчас программа скачивает HTML учебного сайта [Books to Scrape](https://books.toscrape.com/) и извлекает из него данные книг в JSON.

**Начните с [урока 1: Python, Git, HTTP и Requests](docs/lessons/01-http-requests.md)** — создание проекта с нуля и получение HTML. Продолжите [уроком 2: BeautifulSoup и JSON](docs/lessons/02-beautifulsoup.md) — поиск элементов и сохранение структурированных данных.

## Программа обучения

1. Python, Git, HTTP и Requests — скачивание HTML (реализован).
2. BeautifulSoup и извлечение данных — JSON (реализован).
3. Docker.
4. S3 (MinIO).
5. OpenSearch.
6. FastAPI и веб-интерфейс.
7. Docker Compose и объединение системы.

Последующие пять этапов пока не реализованы.

## Что понадобится

Python 3, Git, редактор текста, терминал и интернет для установки зависимостей и загрузки страницы. Проверка установки и инструкции для Windows, Linux и macOS приведены в уроках. Парсер после установки работает с сохранённым HTML без интернета.

## Быстрый запуск готового проекта

В терминале из корня репозитория на Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
python src/parse_books.py
```

В PowerShell на Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/main.py
python src/parse_books.py
```

Первый этап сохраняет исходную страницу в `data/raw/books.html`, второй — список книг в `data/processed/books.json`. При повторном запуске файлы обновляются. Если PowerShell не разрешает активацию, используйте способ без активации из первого урока.

## Учимся по истории

`git log --oneline` показывает коммиты проекта от новых к старым. Изучайте изменения командой `git show <хеш>`; как безопасно открыть старый снимок в отдельной папке, объясняется в [разделе о Git](docs/lessons/01-http-requests.md#часть-3-git-на-практике). Скачанные данные и виртуальное окружение в историю не входят.
