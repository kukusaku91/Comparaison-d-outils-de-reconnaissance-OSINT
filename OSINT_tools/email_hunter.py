import requests
def find_emails(domain, api_key):
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [email["value"] for email in data["data"]["emails"]]
    return []