import threading
from queue import Queue
import socket


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((ip, port))
        with print_lock:
            print('Open ' + ip + ':' + str(port))
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    print_lock = threading.Lock()
    ip = input('Enter ip to scan: ')

    for x in range(30):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    list(map(lambda x: q.put(x), range(1, 65535)))

    q.join()
