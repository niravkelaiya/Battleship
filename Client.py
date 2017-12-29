import socket

class Client(object):

    clientsocket = None

    def create(self):
        self.clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self,port):
        port=int(port)
        self.clientsocket.connect(('127.0.0.1',port))
        print self.receiveMessage()
        self.sendMessage("Client Ready")

    def sendMessage(self,msg):
        self.clientsocket.send(msg)

    def receiveMessage(self):
        while True:
            data = self.clientsocket.recv(1024)
            return data
