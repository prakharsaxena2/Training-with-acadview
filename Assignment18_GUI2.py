from tkinter import *

'''Q1'''
dict = {'Hemant': '9550383917', 'Chetan': '7087331594', 'Devansh': '7248072128', 'Durgesh': '8979122899', 'Shikhar': '8279448505'}
tk = Tk()
f = Frame(master=tk)
f.pack()
scroll = Scrollbar(master=f)
scroll.pack(fill=Y, side=RIGHT)
l = Listbox(f, yscrollcommand=scroll.set)
for key in dict:
    l.insert(END, '{}'.format(key))
l.pack(side=LEFT)
scroll.config(command = l.yview)

'''Q2'''
#Method to add new Contact
def add():
    dict.update({e1.get(): e2.get()})
    for key in dict.keys():
        print(key)
    i = key
    l.insert(END, i)
bottomframe = Frame(tk)
bottomframe.pack(side=BOTTOM)
lbl = Label(bottomframe,text="Enter the name and number: ")
lbl.pack()
e1 = Entry(bottomframe, text="Name")
e2 = Entry(bottomframe, text="Phone No.")
e1.pack()
e2.pack()
btn = Button(master=bottomframe, text="ADD", command=add)
btn.pack()

tk.mainloop()