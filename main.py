import sys
from cloudquery.sdk import serve

from plugin import XKCDPlugin


def main():
    p = XKCDPlugin()
    serve.PluginCommand(p).run(sys.argv[1:])


if __name__ == "__main__":
    main()
