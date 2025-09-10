import json
import os
from cloudquery.sdk import serve
from plugin import ExamplePlugin

def test_plugin_package():
    p = ExamplePlugin()
    cmd = serve.PluginCommand(p)
    cmd.run(["package", "-m", "test", "v0.0.1", "."])
    assert os.path.isfile("dist/tables.json")
    assert os.path.isfile("dist/package.json")
    assert os.path.isfile("dist/docs/overview.md")
    assert os.path.isfile("dist/plugin-example-v0.0.1-linux-amd64.tar")
    assert os.path.isfile("dist/plugin-example-v0.0.1-linux-arm64.tar")

    with open("dist/tables.json", "r") as f:
        tables = json.loads(f.read())
        assert tables == [
            {
                "name": "example_item",
                "title": "Example Item",
                "description": "",
                "is_incremental": False,
                "parent": "",
                "relations": [],
                "columns": [
                    {
                        "name": "num",
                        "type": "uint64",
                        "description": "",
                        "incremental_key": False,
                        "primary_key": True,
                        "not_null": False,
                        "unique": False,
                    },
                    {
                        "name": "string",
                        "type": "string",
                        "description": "",
                        "incremental_key": False,
                        "primary_key": False,
                        "not_null": False,
                        "unique": False,
                    },
                    {
                        "name": "date",
                        "type": "date64[ms]",
                        "description": "",
                        "incremental_key": False,
                        "primary_key": False,
                        "not_null": False,
                        "unique": False,
                    }
                ],
            },
        ]
    with open("dist/package.json", "r") as f:
        package = json.loads(f.read())
        assert package["schema_version"] == 1
        assert package["name"] == "example"
        assert package["version"] == "v0.0.1"
        assert package["team"] == "cloudquery"
        assert package["kind"] == "source"
        assert package["message"] == "test"
        assert package["protocols"] == [3]
        assert len(package["supported_targets"]) == 2
        assert package["package_type"] == "docker"
        assert package["supported_targets"][0]["os"] == "linux"
        assert package["supported_targets"][0]["arch"] == "amd64"
        assert (
            package["supported_targets"][0]["path"]
            == "plugin-example-v0.0.1-linux-amd64.tar"
        )
        assert (
            package["supported_targets"][0]["docker_image_tag"]
            == "docker.cloudquery.io/cloudquery/source-example:v0.0.1-linux-amd64"
        )
        assert package["supported_targets"][1]["os"] == "linux"
        assert package["supported_targets"][1]["arch"] == "arm64"
        assert (
            package["supported_targets"][1]["path"]
            == "plugin-example-v0.0.1-linux-arm64.tar"
        )
        assert (
            package["supported_targets"][1]["docker_image_tag"]
            == "docker.cloudquery.io/cloudquery/source-example:v0.0.1-linux-arm64"
        )
