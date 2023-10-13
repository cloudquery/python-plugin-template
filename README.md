# Python Source Plugin Template
This repo contains everything you need to get started with building a new plugin.
To get started all you need to do is change a few names, define some tables, and write an API Client to populate the tables.

## Key files & classes
 - plugin/tables/items.py
    - Items - A boilerplate table definition
    - ItemResolver - A boilerplate table resolver
 - plugin/example/client.py
  - ExampleClient - A boilerplate API Client
 - plugin/client/client.py
   - Spec - Defines the CloudQuery Config
   - Client (uses: ExampleClient) - Wraps your API Client
 - plugin/plugin.py
   - ExamplePlugin - The plugin registration / how CloudQuery knows what tables your plugin exposes.



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


## Links

- [Architecture](https://www.cloudquery.io/docs/developers/architecture)
- [Concepts](https://www.cloudquery.io/docs/developers/creating-new-plugin/python-source)