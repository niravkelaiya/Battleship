import Tkinter
from Tkinter import *
import socket
import gridpanel
def start():
    counter=0
    port=port_number_box.get()
    try:
        port = int(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost',port))
        s.listen(1)
        conn, addr = s.accept()
        data=conn.recv(1024)
        if data:
            if data=="1":
                print "Client ready"
                conn.send("1")
                g.start()
                root.withdraw()
        conn.close()
        s.close()
    except:
        print "Something went wrong!!Please try again!!"


root = Tk()
root.title("Server connection")
root.geometry("400x400")
g=gridpanel.Grid()
label = Label( root,text="Enter port")
label.grid(row=0,column=0)

port_number_box = Entry(root, bd =5)
port_number_box.grid(row=0,column=3)

startButton = Button(root,text="Start Game",command= lambda: start())
startButton.grid(row=2,column=2)

root.mainloop()
