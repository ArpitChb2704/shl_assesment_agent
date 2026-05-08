import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"


headers = {
    "User-Agent": "Mozilla/5.0"
}


response = requests.get(
    BASE_URL,
    headers=headers
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

catalog = []

links = soup.find_all("a")

visited = set()

for link in links:

    href = link.get("href")

    if not href:
        continue

    if "/products/product-catalog/view/" not in href:
        continue

    full_url = (
        href
        if href.startswith("http")
        else f"https://www.shl.com{href}"
    )

    if full_url in visited:
        continue

    visited.add(full_url)

    try:

        page = requests.get(
            full_url,
            headers=headers
        )

        product_soup = BeautifulSoup(
            page.text,
            "html.parser"
        )

        title = product_soup.find("h1")

        title = (
            title.text.strip()
            if title
            else "Unknown"
        )

        description = product_soup.find("meta", {
            "name": "description"
        })

        description = (
            description.get("content")
            if description
            else ""
        )

        text = description.lower()

        skills = []

        keywords = [
            "java",
            "python",
            "leadership",
            "personality",
            "cognitive",
            "numerical",
            "logical",
            "behavior",
            "communication"
        ]

        for word in keywords:
            if word in text:
                skills.append(word)

        item = {
            "name": title,
            "url": full_url,
            "description": description,
            "test_type": "Unknown",
            "skills": skills
        }

        catalog.append(item)

        print(f"Added: {title}")

    except Exception as e:
        print(e)

with open(
    "data/shl_catalog.json",
    "w"
) as f:

    json.dump(
        catalog,
        f,
        indent=2
    )

print(f"Saved {len(catalog)} assessments")