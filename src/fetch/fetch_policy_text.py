import requests
from bs4 import BeautifulSoup
import re

def fetch_policy_text(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.encoding = resp.apparent_encoding

    soup = BeautifulSoup(resp.text, "html.parser")

    content = soup.find("div", class_=re.compile("content|article|TRS_Editor"))
    text = content.get_text("\n") if content else soup.get_text()

    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()
