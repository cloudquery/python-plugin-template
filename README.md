# Python Source Plugin Template

This repo contains everything you need to get started with building a new plugin.
To get started all you need to do is change a few names, define some tables, and write an API Client to populate the tables.

[![Mastering CloudQuery: How to build a Source Plugin in Python](https://i.ytimg.com/vi/TSbGHz5Z09M/maxresdefault.jpg)](https://youtu.be/TSbGHz5Z09M "Mastering CloudQuery: How to build a Source Plugin in Python")

## Key files & classes

- [plugin/tables/items.py](plugin/tables/items.py)
  - `Items` - A boilerplate table definition
  - `ItemResolver` - A boilerplate table resolver
- [plugin/example/client.py](plugin/example/client.py)
  - `ExampleClient` - A boilerplate API Client
- [plugin/client/client.py]
  - `Spec` - Defines the CloudQuery Config
  - `Client` (uses: `ExampleClient`) - Wraps your API Client
- [plugin/plugin.py](plugin/plugin.py)
  - `ExamplePlugin` - The plugin registration / how CloudQuery knows what tables your plugin exposes.

## Getting started

### Defining your tables

The first thing you need to do is identify the tables you want to create with your plugin.
Conventionally, CloudQuery plugins have a direct relationship between tables and API responses.

For example:
If you had an API endpoint https://api.example.com/items/{num} and for each value of `num` it provided an object

```json
{
   "num": {{num}},
   "date": "2023-10-12",
   "title": "A simple example"
}
```

Then you would design the table class as

```python
class Items(Table):
    def __init__(self) -> None:
        super().__init__(
            name="item",
            title="Item",
            columns=[
                Column("num", pa.uint64(), primary_key=True),
                Column("date", pa.date64()),
                Column("title", pa.string()),
            ],
        )
    ...
```

Creating one table for each endpoint that you want to capture.

### API Client

Next you'll need to define how the tables are retrieved, it's recommended to implement this as a generator, as per the example in `plugin/example/client.py`.

### Spec

Having written your API Client you will have, identified the authentication and/or operational variables needed.
Adding these to the CloudQuery config spec can be done by editing the `Spec` `dataclass` using standard python, and adding validation where needed.

### Plugin

Finally, you need to edit the `plugin.py` file to set the plugin name and version, and add the `Tables` to the `get_tables` function.

### Test run

To test your plugin you can run it locally.

To automatically manage your virtual environment and install the dependencies listed in the `pyproject.toml` you can use `poetry`.
Poetry is an improved package & environment manager for Python that uses the standardised `pyproject.toml`, if you don't have it installed you can pull it with `pip install poetry`.

To install the dependencies into a new virtual environment run `poetry install`.
If you have additional dependencies you can add them with `poetry add {package_name}` which will add them to the `pyproject.toml` and install them into the virtual environment.

Then to run the plugin `poetry run main serve`, which will launch the plugin manually as a GRPC service.

With that running you can adjust the `TestConfig.yaml` to match your plugin and run `cloudquery sync`.
This should result in the creation of a sqlite database `db.sqlite` where you can validate your tables are as expected.

### Publishing

1. Update the plugin metadata in [plugin/plugin.py](plugin/plugin.py#L13) to match your team and plugin name.
2. Run `python main.py package -m "Initial release" "v0.0.1" .`. `-m` specifies changelog and `v0.0.1` is the version.
3. Run `cloudquery plugin publish -f` to publish the plugin to the CloudQuery registry.

> More about publishing plugins [here](https://docs.cloudquery.io/docs/developers/publishing-an-addon-to-the-hub)

## Links

- [Architecture](https://www.cloudquery.io/docs/developers/architecture)
- [Concepts](https://www.cloudquery.io/docs/developers/creating-new-plugin/python-source)
- [Video tutorial](https://youtu.be/TSbGHz5Z09M)
