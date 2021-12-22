import socket
from time import sleep
import threading

host = "192.168.1.1"
ports = []


def scan(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.connect((host, port))
        ports.append([port, "open"])
    except ConnectionRefusedError:
        ports.append([port, "closed"])


def start(n):
    print("scanning")
    li = []

    for port in range(1, n):
        thread = threading.Thread(target=scan, args=(host, port))
        li.append(thread)

    for thread in li:
        thread.start()

    for thread in li:
        thread.join()

    for port, status in sorted(ports):
        if status == "open":
            print(port, "is", status)


# enter number of ports between 1 and 65535
start(1000)

