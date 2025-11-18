import requests


def _convert_github_url_to_raw(url: str) -> str:
    if url.startswith("https://github.com/"):
        url = url.replace("github.com", "raw.githubusercontent.com", 1)
        url = url.replace("blob", "refs/heads", 1)
    return url


def get_deck_from_link(url: str) -> list:
    
    url = _convert_github_url_to_raw(url)
    
    if not url.endswith(".json"):
        return []
    
    response = requests.get(url)    
    if response.status_code != 200:
        return []
    
    try:
        deck = response.json()
        return deck
    
    except requests.exceptions.JSONDecodeError:
        return []

