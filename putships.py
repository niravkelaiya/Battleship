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