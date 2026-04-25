import requests
from requests.auth import HTTPBasicAuth

from src import config


def create_jira_task(summary: str, description: str) -> dict:
    url = f"{config.JIRA_BASE_URL}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": config.JIRA_PROJECT_KEY},
            "summary": summary,
            "issuetype": {"name": config.JIRA_ISSUE_TYPE},
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}],
                    }
                ],
            },
        }
    }

    response = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(config.JIRA_EMAIL, config.JIRA_API_TOKEN),
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        timeout=20,
    )

    response.raise_for_status()
    return response.json()