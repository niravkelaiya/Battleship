    for i in range(0, 10):
        for j in range(14, 24):
            button = Button(m1, command=lambda index=index: change(index))
            button.config(image=im)
            button.grid(row=i, column=j)
            buttons.append(button)
            index += 1