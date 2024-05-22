import requests
from bs4 import BeautifulSoup
from typing import Optional, Any
from datetime import datetime
import os

url = "https://www.theguardian.com/ |football |/article |/2024/may/20/ |arne-slot-liverpool-jurgen-klopp-football"


class GuardianSpider(object):

    def __init__(self, category: Optional[str] = None, subcategory: Optional[str] = None):
        self.base_url: str = "https://www.theguardian.com/international"
        self.category: Optional[str] = category
        self.date = datetime.now().strftime("%Y/%B/%d")
        self.subcategory: Optional[str] = subcategory

    def get_latest_news(self):
        headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        res = requests.get(os.path.join(self.base_url), headers=headers)
        print("site status code : ", res.status_code)

        # response checking
        # f = open("response.html", 'w+')
        # f.write(res.text)
        # f.close()
        with open("response.html", "w", encoding="utf-8") as f:
            f.write(res.text)
            f.close()

        # scrape process
        soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")
        contents = soup.find("div", attrs={"id": "container-headlines"}).find_all("li")

        for content in contents:
            title = content.find("span", attrs={"class": "show-underline"}).text.strip()
            print(title)

    def get_spesific_news(self):
        pass

    def get_news_by_category(self):
        pass

    def get_news_by_subcategory(self):
        pass
