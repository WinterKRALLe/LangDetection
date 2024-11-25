import requests
from bs4 import BeautifulSoup
import re


def harvest_wikipedia(language: str, urls: list) -> str:
    texts = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.text for p in paragraphs)
        # Očištění textu
        text = re.sub(r'[^a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ\s]', '', text)
        text = text.lower()
        texts.append(text)
    return ' '.join(texts)
