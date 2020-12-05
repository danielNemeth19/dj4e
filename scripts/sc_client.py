import socket


def make_connection():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(('127.0.0.1', 8000))
    cmd = 'GET /index/ HTTP/1.1\r\n\r\n'.encode()
    my_socket.send(cmd)

    while True:
        data = my_socket.recv(512).decode()
        if data.startswith("HTTP/1.1 200 OK"):
            print(data, end='')
            break

    my_socket.shutdown(socket.SHUT_RDWR)
    my_socket.close()


if __name__ == "__main__":
    make_connection()
