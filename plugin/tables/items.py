from typing import Any, Generator

import pyarrow as pa
from cloudquery.sdk.scheduler import TableResolver
from cloudquery.sdk.schema import Column
from cloudquery.sdk.schema import Table
from cloudquery.sdk.schema.resource import Resource

from plugin.client import Client


class Items(Table):
    def __init__(self) -> None:
        super().__init__(
            name="example_item",
            title="Example Item",
            columns=[
                Column("num", pa.uint64(), primary_key=True),
                Column("string", pa.string()),
                Column("date", pa.date64()),
            ],
        )

    @property
    def resolver(self):
        return ItemResolver(table=self)


class ItemResolver(TableResolver):
    def __init__(self, table) -> None:
        super().__init__(table=table)

    def resolve(
        self, client: Client, parent_resource: Resource
    ) -> Generator[Any, None, None]:
        for item_response in client.client.item_iterator():
            yield item_response
