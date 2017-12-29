from Tkinter import *
class Grid:
    labels = []
    buttons=[]
    m1=Tk()
    im3 = PhotoImage(file="C:\Users\Crest\Downloads\ship.GIF")
    ship1=[1,11,21,31]
    def change(self,index):
        self.buttons[index].config(state="disabled")
        # m2 = Tk()
        # label1 = Label(m2, text="Waiting for player's move")
        # label1.configure(background="yellow")
        # label1.grid(row=5,column=5)
        # m2.focus_force()
        self.m1.withdraw()
       # m1.after(5000)
       # m2.destroy()
        self.m1.deiconify()
        self.putships()

    def putships(self):
        i = 0
        index = 0
        for label in self.labels:
            if i==len(self.ship1):
                break
            if index == self.ship1[i]:
                label.config(image=self.im3)
                i += 1
            index += 1
    def start(self):
        im1 = PhotoImage(file="C:\Users\Crest\Downloads\shortline.GIF")
        im = PhotoImage(file="C:\Users\Crest\Downloads\labelimg.GIF")
        self.m1.geometry('1053x470+130+130')
        indexl = 0
        for i in range(0, 10):
            for j in range(0, 11):
                if j == 10:
                    line = Label(self.m1)
                    line.config(image=im1)
                    line.grid(row=i, column=11)
                else:
                    left = Label(self.m1)
                    left.config(image=im)
                    left.grid(row=i, column=j)
                    self.labels.append(left)
                    indexl += 1
        index = 0
        for i in range(0, 10):
            for j in range(14, 24):
                button = Button(self.m1, command=lambda index=index: self.change(index))
                button.config(image=im)
                button.grid(row=i, column=j)
                self.buttons.append(button)
                index += 1
        head1 = Label(self.m1, text="Your", font="Times 12 bold")
        head2 = Label(self.m1, text="Board", font="Times 12 bold")
        head3 = Label(self.m1, text="Attack", font="Times 12 bold")
        head4 = Label(self.m1, text="Board", font="Times 12 bold")
        head1.grid(row=i + 4, column=5)
        head2.grid(row=i + 4, column=6)
        head3.grid(row=i + 4, column=17)
        head4.grid(row=i + 4, column=18)
        mainloop()

# m1 = Tk()
# im1 = PhotoImage(file="C:\Users\Crest\Downloads\shortline.GIF")
# im=PhotoImage(file="C:\Users\Crest\Downloads\labelimg.GIF")
# im3=PhotoImage(file="C:\Users\Crest\Downloads\ship.GIF")
# m1.geometry('1053x470+130+130')
# labels=[]
# indexl=0
# for i in range(0,10):
#     for j in range(0,11):
#         if j==10:
#             line = Label(m1)
#             line.config(image=im1)
#             line.grid(row=i,column=11)
#         else:
#             left = Label(m1)
#             left.config(image=im)
#             left.grid(row=i,column=j)
#             labels.append(left)
#             indexl+=1
# index=0
# buttons=[]
# for i in range(0,10):
#     for j in range(14,24):
#         button = Button(m1,command=lambda index=index:change(index))
#         button.config(image=im)
#         button.grid(row=i,column=j)
#         buttons.append(button)
#         index+=1
# head1=Label(m1,text="Your", font="Times 12 bold")
# head2=Label(m1,text="Board", font="Times 12 bold")
# head3=Label(m1,text="Attack", font="Times 12 bold")
# head4=Label(m1,text="Board", font="Times 12 bold")
# head1.grid(row=i+4,column=5)
# head2.grid(row=i+4,column=6)
# head3.grid(row=i+4,column=17)
# head4.grid(row=i+4,column=18)
#
# ship1=[1,11,21,31]
# mainloop()
