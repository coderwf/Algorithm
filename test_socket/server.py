
# -*- coding:utf-8 -*-

import socket
import threading
class ListenThread(threading.Thread):
    def __init__(self,ip,port,handle):
        threading.Thread.__init__(self)
        self.ip      = ip
        self.port    = port
        self.handle  = handle
    def run(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind((self.ip,self.port))
        sock.listen(5)
        while True:
            con , addr = sock.accept()
            self.handle.process(con,addr)


if __name__ == "__main__":
    lthread = ListenThread("localhost",9000)
    lthread.start()
    lthread = ListenThread("localhost", 9000)
    lthread.start()