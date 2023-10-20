from typing import Generator, Dict, Any
from urllib.parse import urljoin

import requests


class ComicsClient:
    def __init__(self, base_url="https://xkcd.com"):
        self._base_url = base_url

    def comic_iterator(self) -> Generator[Dict[str, Any], None, None]:
        response = requests.get(urljoin(self._base_url, "info.0.json"))
        if response.status_code != 200:
            raise ValueError("Bad HTTP Response")
        yield response.json()

        num = response.json().get("num", 0)
        while num > 0:
            num -= 1
            response = requests.get(urljoin(urljoin(self._base_url, f"/{num}/"), "info.0.json"))
            if response.status_code != 200:
                raise ValueError("Bad HTTP Response")
            yield response.json()
