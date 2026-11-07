from pathlib import Path
import json
import sys
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup


BASE_URL = "https://books.toscrape.com/"
PROJECT_DIR = Path(__file__).resolve().parent.parent
HTML_FILE = PROJECT_DIR / "data" / "raw" / "books.html"
JSON_FILE = PROJECT_DIR / "data" / "processed" / "books.json"


def main():
    try:
        html = HTML_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("HTML не найден. Сначала запустите: python src/main.py", file=sys.stderr)
        return 1
    except (OSError, UnicodeError) as error:
        print(f"Не удалось прочитать HTML: {error}", file=sys.stderr)
        return 1

    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select("article.product_pod")
    if not cards:
        print("Карточки книг не найдены. Проверьте HTML и селектор.", file=sys.stderr)
        return 1

    books = []
    for number, card in enumerate(cards, start=1):
        link = card.select_one("h3 a")
        price = card.select_one("p.price_color")
        availability = card.select_one("p.availability")

        if not link or not link.get("title") or not link.get("href") or not price or not availability:
            print(f"Карточка {number}: отсутствует название, ссылка, цена или наличие.", file=sys.stderr)
            return 1

        title = link.get("title").strip()
        href = link.get("href").strip()
        price_text = price.get_text(strip=True)
        availability_text = availability.get_text(strip=True)
        if not title or not href or not price_text or not availability_text:
            print(f"Карточка {number}: одно из полей пустое.", file=sys.stderr)
            return 1

        try:
            url = urljoin(BASE_URL, href)
            parsed_url = urlsplit(url)
            if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
                raise ValueError("ожидалась HTTP-ссылка")
        except ValueError as error:
            print(f"Карточка {number}: некорректная ссылка: {error}", file=sys.stderr)
            return 1

        books.append({
            "title": title,
            "price": price_text,
            "availability": availability_text,
            "url": url,
        })

    try:
        JSON_FILE.parent.mkdir(parents=True, exist_ok=True)
        with JSON_FILE.open("w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Не удалось сохранить JSON: {error}", file=sys.stderr)
        return 1

    print(f"Найдено книг: {len(books)}. JSON сохранён в {JSON_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
