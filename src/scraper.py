import requests
from bs4 import BeautifulSoup


def scrape_page_title(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return {
        "id": url,
        "title": soup.title.text.strip() if soup.title else "No title",
        "url": url,
    }

if __name__ == "__main__":
    item = scrape_page_title("https://pizzafredag.dk/tilbud/")
    print(type(item["id"]))




