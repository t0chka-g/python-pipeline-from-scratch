from pathlib import Path
import sys

import requests


URL = "https://books.toscrape.com/"
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "raw" / "books.html"


def main():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_bytes(response.content)
    except requests.exceptions.Timeout:
        print("Ошибка: сайт не ответил вовремя.", file=sys.stderr)
        return 1
    except requests.exceptions.HTTPError as error:
        print(f"Ошибка HTTP: {error}", file=sys.stderr)
        return 1
    except requests.exceptions.RequestException as error:
        print(f"Ошибка сети: {error}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Не удалось сохранить файл: {error}", file=sys.stderr)
        return 1

    print(f"Готово: HTML сохранён в {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
