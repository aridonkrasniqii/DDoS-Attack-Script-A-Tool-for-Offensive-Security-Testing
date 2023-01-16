import argparse
from argparse import ArgumentParser

# Specified commands
def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', nargs="?", help="Web server,  [gjirafa50.com]", required=True)
    parser.add_argument('-d', '--dir', default="", help="Web path, [admin/index.php] (Default: /)")
    parser.add_argument('-s', '--ssl', dest="ssl", action="store_false", help="HTTP/HTTPS")
    parser.add_argument('-p', '--port', default=80, help="Port #, [80 or 443] (Default 80)", type=int)
    parser.add_argument('-t', '--threads', default=100, help="Number of threads (Default 100)", type=int)
    parser.add_argument('-x', '--proxy_file', help="File text for proxy (Opcionale)")
    return parser.parse_args()

