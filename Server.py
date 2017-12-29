import socket

class Server(object):

    serversocket = None
    c = None
    addr = None
    data = ""

    def create(self,port):
        self.serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serversocket.bind(('',int(port)))
        self.serversocket.listen(1)

    def connect(self):
        self.c, self.addr = self.serversocket.accept()
        self.sendMessage("Server Connected")
        print self.receiveMessage()

    def sendMessage(self,msg):
        self.c.send(msg)

    def receiveMessage(self):
        while True:
            data = self.c.recv(1024)
            return data
