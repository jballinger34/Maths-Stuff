from tkinter import *

#setting up window

root = Tk()
root.title("Scientific Calculator")

WIDTH, HEIGHT = "1000", "800"
root.geometry(WIDTH + "x" + HEIGHT)

#functions definitions
def TopLineText(currenttext,operation):
    text = ""
    return text

def InsertNum(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(num))

def Clear():
    e.delete(0,END)

def Delete():
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)[:-1])




#top box and entrybox

topBox = Label(root) ##needs work
topBox.grid(row=0, column=0)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=1, column=0)

#numpad

numpad = Frame()
numpad.grid(row=2,column=0, padx=100, pady=10)

for i in range(0,10):
    if i%3 == 0:
        colnumber= 3
    else:
        colnumber = i%3
    if i/3 == 0:
        rownumber = 4
        colnumber = 2
    elif i/3 <= 1:
        rownumber = 1
    elif i/3 <= 2:
        rownumber = 2
    else:
        rownumber = 3
    button = Button(numpad, text=i, padx=40, pady=20, command=lambda i=i: InsertNum(i))
    button.grid(row= rownumber ,column= colnumber)

def DecimalPlace():
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + ".")


decimalPlace = Button(numpad, text=".",padx=40, pady=20, command=lambda: DecimalPlace())
decimalPlace.grid(row=4,column=3)

#bottom right box

bottomRight = Frame()
bottomRight.grid(row=2, column=1)

clearButton = Button(bottomRight, text="Clear", padx=40, pady=20, command=lambda: Clear())
clearButton.grid(row= 0 ,column= 0 , columnspan=2)

deleteButton = Button(bottomRight, text="Delete", padx=40, pady=20, command=lambda: Delete())
deleteButton.grid(row=1, column= 0, columnspan= 2)






#.mainloop

root.mainloop()