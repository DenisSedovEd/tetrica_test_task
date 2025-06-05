import aiohttp
import asyncio
from bs4 import BeautifulSoup
import aiofiles

BASE_URL = "https://ru.wikipedia.org"
START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"
OUTPUT_FILE = "beasts.csv"
MAX_PAGES = 150


async def fetch(session, url):
    async with session.get(url) as resp:
        text = await resp.text(encoding="utf-8")
        return text


async def get_all_pages(session, max_pages):
    urls = [START_URL]
    seen = set(urls)
    current_url = START_URL
    count = 1
    while count < max_pages:
        text = await fetch(session, current_url)
        soup = BeautifulSoup(text, "html.parser")
        next_link = soup.select_one('a:-soup-contains("Следующая страница")')
        if next_link:
            next_url = BASE_URL + next_link["href"]
            if next_url in seen:
                break
            urls.append(next_url)
            seen.add(next_url)
            current_url = next_url
            count += 1
        else:
            break
    return urls


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    result = {}
    for group in soup.select("div.mw-category-group"):
        letter_header = group.find("h3")
        if not letter_header:
            continue
        letter = letter_header.text.strip()
        items = group.find_all("li")
        result[letter] = result.get(letter, 0) + len(items)
    return result


async def main():
    async with aiohttp.ClientSession() as session:
        print(f"Собираем до {MAX_PAGES} страниц...")
        urls = await get_all_pages(session, MAX_PAGES)
        print(f"Всего страниц: {len(urls)}. Загружаем параллельно...")

        tasks = [fetch(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)

        animals_per_letter = {}
        for html in pages:
            page_counts = parse_page(html)
            for letter, count in page_counts.items():
                animals_per_letter[letter] = animals_per_letter.get(letter, 0) + count

        sorted_items = sorted(animals_per_letter.items(), key=lambda x: x[0])
        async with aiofiles.open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
            for letter, count in sorted_items:
                line = f"{letter},{count}\n"
                await f.write(line)
        print(f"Готово: данные записаны в {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
