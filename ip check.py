import socket
hostn = socket.gethostname()
IPAD = socket.gethostbyname(hostn)
print("IP address is:" +IPAD)