if hit==1:
        labels[co].config(image=im4)
        s.sendMessage("1")
    else:
        labels[co].config(image=im5)
        s.sendMessage("0")