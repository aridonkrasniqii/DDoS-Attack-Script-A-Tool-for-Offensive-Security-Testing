import urllib.request

# Function that tells if website is protected by cloudflare
def cloudflare(url):
    cf_message = False
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    response = urllib.request.urlopen(req)
    if "CF-Cache-Status: HIT" in str(response.info()):
        cf_message = True
    return cf_message
