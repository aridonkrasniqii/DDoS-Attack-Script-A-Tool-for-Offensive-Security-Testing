import urllib.request
import requests

import urllib 

# Function that tells if website is protected by cloudflare
def cloudflare(url):
    # This function is not reliable because Cloudflare is not reliable as cloudflare can change its headers 
    cf_message = False
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'})
    response = urllib.request.urlopen(req)
    if "CF-Cache-Status: HIT" in str(response.info()):
        cf_message = True

    return cf_message



def check_cloudflare(url): 
      
    try:
        res = requests.get(url)
        server = res.headers.get('Server')
        cf_ray = res.headers.get('cf-ray')
        if server and 'cloudflare' in server.lower() and cf_ray:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(e)


