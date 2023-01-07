import argparse


# Specified commands
def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', nargs="?", help="Web serveri, p.sh: coinmarketcap.com", required=True)
    parser.add_argument('-d', '--dir', default="", help="Web path, p.sh: admin/index.php (Default: /)")
    parser.add_argument('-s', '--ssl', dest="ssl", action="store_false", help="HTTP/HTTPS")
    parser.add_argument('-p', '--port', default=80, help="Port #, 80 ose 443 (Default 80)", type=int)
    parser.add_argument('-t', '--threads', default=100, help="Numri i fijeve/threads (Default 100)", type=int)
    parser.add_argument('-x', '--proxy_file', help="Tekst fajlli per proxy (Opcionale)")
    return parser.parse_args()

