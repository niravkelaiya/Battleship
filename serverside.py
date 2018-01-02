import Tkinter
from Tkinter import *
import tkMessageBox
import Server

from threading import Thread

def start():
    s.create(port_number_box.get())
    s.connect()
    root.destroy()
    location()
    play(mainlist)

def location():
    root=Tk()
    root.focus_force()
    root.title("Location of Boats")
    label_for_carrier = Label(root,text="Carrier")
    label_for_battleship = Label(root,text="Battleship")
    label_for_cruiser = Label(root,text="Cruiser")
    label_for_submarine = Label(root,text="Submarine")
    label_for_destroyer = Label(root,text="Destroyer")

    var_carrier1 = StringVar(root)
    var_carrier2 = StringVar(root)
    var_battleship1 = StringVar(root)
    var_battleship2 = StringVar(root)
    var_cruiser1 = StringVar(root)
    var_cruiser2 = StringVar(root)
    var_submarine1 = StringVar(root)
    var_submarine2 = StringVar(root)
    var_destroyer1 = StringVar(root)
    var_destroyer2 = StringVar(root)

    var_destroyer1.set("0")
    var_destroyer2.set("0")
    var_submarine2.set("0")
    var_submarine1.set("0")
    var_cruiser2.set("0")
    var_cruiser1.set("0")
    var_battleship2.set("0")
    var_battleship1.set("0")
    var_carrier1.set("0")
    var_carrier2.set("0")

    option_carrierx = OptionMenu(root, var_carrier1, "0", "1","2","3","4","5","6","7","8","9")
    option_carrierx.grid(row=0, column=1)

    option_carriery = OptionMenu(root, var_carrier2, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_carriery.grid(row=0, column=2)

    option_battleshipx = OptionMenu(root, var_battleship1, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_battleshipx.grid(row=1, column=1)

    option_battleshipy = OptionMenu(root, var_battleship2, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_battleshipy.grid(row=1, column=2)

    option_cruiserx = OptionMenu(root, var_cruiser1, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_cruiserx.grid(row=2, column=1)

    option_cruisery = OptionMenu(root, var_cruiser2, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_cruisery.grid(row=2, column=2)

    option_submarinex = OptionMenu(root, var_submarine1, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_submarinex.grid(row=3, column=1)

    option_submariney = OptionMenu(root, var_submarine2, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_submariney.grid(row=3, column=2)

    option_destroyerx = OptionMenu(root, var_destroyer1, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_destroyerx.grid(row=4, column=1)

    option_destroyery = OptionMenu(root, var_destroyer2, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    option_destroyery.grid(row=4, column=2)

    label_for_battleship.grid(row=1)
    label_for_carrier.grid(row=0)
    label_for_cruiser.grid(row=2)
    label_for_submarine.grid(row=3)
    label_for_destroyer.grid(row=4)

    var1 = StringVar(root)
    var2 = StringVar(root)
    var3 = StringVar(root)
    var4 = StringVar(root)
    var5 = StringVar(root)

    var1.set("Horizontal")
    var2.set("Horizontal")
    var3.set("Horizontal")
    var4.set("Horizontal")
    var5.set("Horizontal")

    option_carrier = OptionMenu(root, var1, "Horizontal", "Vertical")
    option_carrier.grid(row=0,column=3)

    option_battleship = OptionMenu(root, var2, "Horizontal", "Vertical")
    option_battleship.grid(row=1, column=3)

    option_cruiser = OptionMenu(root, var3, "Horizontal", "Vertical")
    option_cruiser.grid(row=2, column=3)

    option_submarine = OptionMenu(root, var4, "Horizontal", "Vertical")
    option_submarine.grid(row=3, column=3)

    option_destroyer = OptionMenu(root, var5, "Horizontal", "Vertical")
    option_destroyer.grid(row=4, column=3)

    def calculate(var1,var2,var3,var4):
        list1=[]
        counter=0
        pos = var1.get()
        x = var2.get()
        y = var3.get()
        if pos == "Horizontal":
            if int(y)+var4-1 <=9:
                for i in range(0,var4):
                    list1.append(int(x)*10 + int(y)+counter)
                    counter+=1
            else:
                tkMessageBox.showerror(title="Error",
                                       message="Boats can't be broken!!:)!! Please enter proper coordinates!!")
                return False
        else:
            if int(x) + var4-1 < 9:
                for i in range(0, var4):
                    list1.append((int(x)+counter) * 10 + int(y))
                    counter += 1
            else:
                tkMessageBox.showerror(title="Error",
                                       message="Boats can't be broken!!:)!! Please enter proper coordinates!!")
                return False

        if bool(set(mainlist) & set(list1)):
            tkMessageBox.showerror(title="Error",message="Boats are overlapping!! Please enter proper coordinates")
            return False
        else:
            mainlist.extend(list1)
            return True

    def getDetails():
        del mainlist[:]
        if calculate(var1,var_carrier1,var_carrier2,5):
            if calculate(var2, var_battleship1, var_battleship2,4):
                if calculate(var3, var_cruiser1, var_cruiser2,3):
                    if calculate(var4, var_submarine1, var_submarine2,3):
                        if calculate(var5, var_destroyer1, var_destroyer2,2):
                            root.destroy()



    submit_button = Button(root,text="Place",command=getDetails)
    submit_button.grid(columnspan=3)

def restart():
    location()
    play(mainlist)

def change(index):
    buttons[index].config(state="disabled")
    clicked.append(buttons[index])
    s.sendMessage(str(index))
    hit=0
    co = s.receiveMessage()
    if co=="111":
        m1.destroy()
        w1 = Tk()
        res = Label(w1, text="You Won server", font="Times 18 bold")
        res.grid(row=0,column=0)
        restart = Button(w1, text="Restart", command=lambda:restart)
        restart.grid(row=1, column=1)
        return
    co=int(co)
    co = co % 100
    for i in mainlist:
        if i ==co:
            mainlist.remove(i)
            if len(mainlist)==0:
                m1.destroy()
                w1=Tk()
                res = Label(w1, text="You Lost sever", font="Times 18 bold")
                res.grid(row=0, column=0)
                s.sendMessage("111")
                restart = Button(w1, text="Restart", command=lambda:restart)
                restart.grid(row=1, column=1)
                return
                break
            hit=1
    if hit==1:
        labels[co].config(image=im4)
        s.sendMessage("1")
    else:
        labels[co].config(image=im5)
        s.sendMessage("0")
    co=s.receiveMessage()
    if co=='1':
        buttons[index].config(image=im4)
    else:
        buttons[index].config(image=im5)

def putships(list1):
    i = 0
    index = 0
    list1.sort()
    for button in buttons:
        if button not in list1:
            button.config(state="normal")
    for label in labels:
        if i==len(list1):
            break
        if index == list1[i]:
            label.config(image=im3)
            i += 1
        index += 1
def play(list1):
    m1.deiconify()
    indexl = 0
    for i in range(0, 10):
        for j in range(0, 11):
            if j == 10:
                line = Label(m1)
                line.config(image=im1)
                line.grid(row=i, column=11)
            else:
                left = Label(m1)
                left.config(image=im)
                left.grid(row=i, column=j)
                labels.append(left)
                indexl += 1
    index = 0
    for i in range(0, 10):
        for j in range(14, 24):
            button = Button(m1, command=lambda index=index: change(index))
            button.config(image=im)
            button.grid(row=i, column=j)
            buttons.append(button)
            index += 1
    head1 = Label(m1, text="Your", font="Times 12 bold")
    head2 = Label(m1, text="Board", font="Times 12 bold")
    head3 = Label(m1, text="Attack", font="Times 12 bold")
    head4 = Label(m1, text="Board", font="Times 12 bold")
    ready = Button(m1, text="Start", font="Times 12 bold",command=lambda l=list1:putships(l))
    head1.grid(row=i + 4, column=5)
    head2.grid(row=i + 4, column=6)
    head3.grid(row=i + 4, column=17)
    head4.grid(row=i + 4, column=18)
    ready.grid(row=i+3,column=11)
    mainloop()


labels = []
mainlist=[]
buttons=[]
clicked=[]
m1=Tk()
m1.title(" server grid")
m1.withdraw()
im1 = PhotoImage(file="C:\Users\Crest\Downloads\shortline.GIF")
im = PhotoImage(file="C:\Users\Crest\Downloads\labelimg.GIF")
im3 = PhotoImage(file="C:\Users\Crest\Downloads\ship.GIF")
im4 = PhotoImage(file="C:\Users\Crest\Downloads\hit.GIF")
im5 = PhotoImage(file="C:\Users\Crest\Downloads\miss.GIF")
label1 = Label(m1, text="Waiting for player's move", font="Times 12 bold", background="yellow")
#g=gridpanel.Grid()
s = Server.Server()
root = Tk()
root.geometry("400x400")
root.title("Client connection")
label = Label( root,text="Enter port number")
label.grid(row=0,column=0)

port_number_box = Entry(root, bd =5)
port_number_box.grid(row=0,column=3)

startButton = Button(root,text="Start The Game",command=start)
startButton.grid(row=2,column=2)

root.mainloop()