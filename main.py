import sys
from cloudquery.sdk import serve

from plugin import ExamplePlugin


def main():
    p = ExamplePlugin()
    serve.PluginCommand(p).run(sys.argv[1:])


if __name__ == "__main__":
    main()
