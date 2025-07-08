"""Simple web scraper for obtaining job descriptions."""
from typing import List
import requests
from bs4 import BeautifulSoup


USER_AGENT = "Mozilla/5.0"


def scrape_job_descriptions(query: str, limit: int = 5) -> List[str]:
    """Scrape remote job listings from RemoteOK based on a query."""
    url = f"https://remoteok.com/remote-{query.replace(' ', '-')}-jobs"
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=10)
        resp.raise_for_status()
    except requests.RequestException:
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    jobs: List[str] = []
    for card in soup.select("td.company_and_position"):  # type: ignore[arg-type]
        title = card.select_one("h2")
        if title:
            jobs.append(title.get_text(strip=True))
        if len(jobs) >= limit:
            break
    return jobs
