import urllib.request

file_handler = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
for line in file_handler:
    print(line.decode().strip())
