import Tkinter
from Tkinter import *
import tkMessageBox

mainlist=[]


def location():
    root=Tk()
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

    root.mainloop()
    return mainlist