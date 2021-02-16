import socket
from tabulate import tabulate

class Network_Info(object):
    def __init__(self,url="www.youtube.com"):
        self.url=url
        #get my ip#
        self.host_name = socket.gethostname()
        self.ip_add= socket.gethostbyname(self.host_name)
        self.remot_ip = self.remot_information()

    def __repr__(self):
        data={"host name:": [self.host_name],
              "ip @:": [self.ip_add],
              f"{self.url}:": [self.remot_ip]}
        table = tabulate(data, headers="keys", tablefmt="grid")
        return table

    def remot_information(self):
        try:
            return socket.gethostbyname(self.url)
        except socket.error as error:
            return error

if __name__=="__main__":
    print(Network_Info())