# Python pipeline from scratch

Цель проекта — шаг за шагом научиться создавать Python-приложение и понимать инструменты вокруг него. Каждый урок продолжает один и тот же проект. Сейчас реализован только первый урок: программа получает HTML учебного сайта [Books to Scrape](https://books.toscrape.com/).

**Начните с [урока 1: Python, Git, HTTP и Requests](docs/lessons/01-http-requests.md)** — в нём есть создание проекта с нуля, объяснение кода и задания.

## Программа обучения

1. Python, Git, HTTP и Requests — скачивание HTML.
2. BeautifulSoup и извлечение данных.
3. Docker.
4. S3 (MinIO).
5. OpenSearch.
6. FastAPI и веб-интерфейс.
7. Docker Compose и объединение системы.

Последующие этапы пока не реализованы.

## Что понадобится

Python 3, Git, редактор текста, терминал и интернет для установки Requests и запроса к сайту. Проверка установки и инструкции для Windows, Linux и macOS приведены в уроке.

## Быстрый запуск готового проекта

В терминале из корня репозитория на Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```

В PowerShell на Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/main.py
```

Результат — `data/raw/books.html`. Если PowerShell не разрешает активацию, используйте способ без активации из урока.

## Учимся по истории

`git log --oneline` показывает коммиты проекта от новых к старым. Изучайте изменения командой `git show <хеш>`; как безопасно открыть старый снимок в отдельной папке, объясняется в [разделе о Git](docs/lessons/01-http-requests.md#часть-3-git-на-практике). Скачанные данные и виртуальное окружение в историю не входят.
