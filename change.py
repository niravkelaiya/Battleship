def change(index):
    buttons[index].config(state="disabled")
    clicked.append(buttons[index])
    s.sendMessage(str(index))
    hit=0
    co = s.receiveMessage()
    co=int(co)
    co = co % 100
    for i in mainlist:
        if i ==co:
            mainlist.remove(i)
            if len(mainlist)==0:
                m1.destroy()
                w1=Tk()
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
        buttons[index].config(image=im5