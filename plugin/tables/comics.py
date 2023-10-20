from typing import Any, Generator

import pyarrow as pa
from cloudquery.sdk.scheduler import TableResolver
from cloudquery.sdk.schema import Column
from cloudquery.sdk.schema import Table
from cloudquery.sdk.schema.resource import Resource

from plugin.client import Client


class Comics(Table):
    """{
        "month": "10",
        "num": 2841,
        "link": "",
        "year": "2023",
        "news": "",
        "safe_title": "Sign Combo",
        "transcript": "",
        "alt": "Speed Limit: 45 MPH / Minimum: 65 MPH",
        "img": "https://imgs.xkcd.com/comics/sign_combo.png",
        "title": "Sign Combo",
        "day": "13"
    }"""
    def __init__(self) -> None:
        super().__init__(
            name="cq_comics",
            title="Comics",
            columns=[
                Column("num", pa.uint64(), primary_key=True),
                Column("year", pa.string()),
                Column("month", pa.string()),
                Column("day", pa.string()),
                Column("safe_title", pa.string()),
                Column("title", pa.string()),
                Column("news", pa.string()),
                Column("transcript", pa.string()),
                Column("alt", pa.string()),
                Column("img", pa.string()),
            ],
        )

    @property
    def resolver(self):
        return ComicResolver(table=self)


class ComicResolver(TableResolver):
    def __init__(self, table) -> None:
        super().__init__(table=table)

    def resolve(
        self, client: Client, parent_resource: Resource
    ) -> Generator[Any, None, None]:
        for comic_response in client.client.comic_iterator():
            yield comic_response
