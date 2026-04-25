from src import config
from src.scraper import scrape_page_title
from src.state import load_state, save_state
from src.jira_client import create_jira_task


def main():
    item = scrape_page_title(config.TARGET_URL)

    state = load_state()

    if item["id"] in state:
        print("Intet nyt fundet.")
        return

    issue = create_jira_task(
        summary=f"Nyt fund: {item['title']}",
        description=f"Fundet på: {item['url']}",
    )

    state[item["id"]] = {
        "title": item["title"],
        "url": item["url"],
        "jira_issue": issue.get("key"),
    }

    save_state(state)

    print(f"Oprettet Jira task: {issue.get('key')}")


if __name__ == "__main__":
    main()