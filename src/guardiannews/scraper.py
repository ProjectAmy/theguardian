import requests
from bs4 import BeautifulSoup
from typing import Optional, Any

url = "https://www.theguardian.com/ |football |/article |/2024/may/20/ |arne-slot-liverpool-jurgen-klopp-football"

class GuardianSpider(object):

    def __init__(self, category: Optional[str]=None):

        self.base_url: str = "https://www.theguardian.com"
        self.category: str = category
        self.date =