from dataclasses import dataclass, field
from cloudquery.sdk.scheduler import Client as ClientABC

from plugin.comics.client import ComicsClient

DEFAULT_CONCURRENCY = 100
DEFAULT_QUEUE_SIZE = 10000


@dataclass
class Spec:
    base_url: str = field(default="https://xkcd.com")
    concurrency: int = field(default=DEFAULT_CONCURRENCY)
    queue_size: int = field(default=DEFAULT_QUEUE_SIZE)

    def validate(self):
        pass
        # if self.access_token is None:
        #     raise Exception("access_token must be provided")


class Client(ClientABC):
    def __init__(self, spec: Spec) -> None:
        self._spec = spec
        self._client = ComicsClient(spec.base_url)

    def id(self):
        return "xkcd"

    @property
    def client(self) -> ComicsClient:
        return self._client
