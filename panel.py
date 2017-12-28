from Tkinter import *

def change(index):
    buttons[index].config(state="disabled")

m1 = Tk()
im1 = PhotoImage(file="C:\Users\Crest\Downloads\shortline.GIF")
im=PhotoImage(file="C:\Users\Crest\Downloads\labelimg.GIF")
m1.geometry('730x570+50+50')
for i in range(0,10):
    for j in range(0,11):
        if j==10:
            line = Label(m1)
            line.config(image=im1)
            line.grid(row=i,column=11)
        else:
            left = Label(m1)
            left.config(image=im)
            left.grid(row=i,column=j)

index=0
buttons=[]
for i in range(0,10):
    for j in range(13,23):
        button = Button(m1,command=lambda index=index:change(index))
        button.config(image=im)
        button.grid(row=i,column=j)
        buttons.append(button)
        index+=1
mainloop()