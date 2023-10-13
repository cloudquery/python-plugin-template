from typing import Generator, Dict, Any


class ExampleClient:
    def __init__(self, access_token, base_url="https://api.example.com"):
        self._access_token = access_token
        self._base_url = base_url

    def item_iterator(self, page: int = 1) -> Generator[Dict[str, Any], None, None]:
        ...
