import socket as s 
host = input('enter your web that search IP \n')
print(f'IP of {host} is {s.gethostbyname(host)}')