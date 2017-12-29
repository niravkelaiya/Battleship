import Tkinter
from Tkinter import *
import socket
import gridpanel


def start():
    counter=0
    port=port_number_box.get()
    try:
        port=int(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost',port))
        s.send("1")
        data=s.recv(1024)
        if data:
            if data=="1":
                print "Server ready"
                g.start()
                root.withdraw()
    except:
        print "Something went wrong!!Please try again!!"


root = Tk()
root.geometry("400x400")
root.title("Client connection")
g=gridpanel.Grid()
label = Label( root,text="Enter port number")
label.grid(row=0,column=0)

port_number_box = Entry(root, bd =5)
port_number_box.grid(row=0,column=3)

startButton = Button(root,text="Start The Game",command= lambda: start())
startButton.grid(row=2,column=2)

root.mainloop()
