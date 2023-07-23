# followed this guide to extract and setup the tkinterdnd package
# https://www.delftstack.com/howto/python-tkinter/tkinter-drag-and-drop/

from tkinter import *
from TkinterDnD2 import *

def path_listbox(event):
    listbox.insert("end", event.data)

window = TkinterDnD.Tk()
# window.title('Delftstack')
# window.geometry('400x300')
# window.config(bg='gold')
frame = Frame(window)
frame.pack()

# ------------------------------------------------------------------------------------
# drag drop to list widget

# listbox setup
listbox = Listbox( frame, width=50, height=15, selectmode=SINGLE )
listbox.insert(0, "item 1")
listbox.insert(1, "item 2")

listbox.pack(fill=X, side=LEFT)
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', path_listbox)

# scrollbar setup
scrolbar= Scrollbar(frame,orient=VERTICAL)
scrolbar.pack(side=RIGHT, fill=Y)

# displays the content in listbox
listbox.configure(yscrollcommand=scrolbar.set)

# view the content vertically using scrollbar
scrolbar.config(command=listbox.yview)

# ------------------------------------------------------------------------------------
# drag drop to input / entry widget

def DropFile(event):
    testvariable.set(event.data)
    print(testvariable.get())

testvariable = StringVar()
textlabel=Label(window, text='drop the file here', bg='#fcba03')
textlabel.pack(anchor=NW, padx=10)
entrybox = Entry(window, textvar=testvariable, width=80)
entrybox.pack(fill=X, padx=10)
entrybox.drop_target_register(DND_FILES)
entrybox.dnd_bind('<<Drop>>', DropFile)


# ------------------------------------------------------------------------------------
# button which prints all list values and text entry values

def print_list_values():
    # print(listbox.get(0 , END))
    for key in listbox.get(0 , END):
        print(key)

def print_selected_list_value():
    print(listbox.curselection())
    for i in listbox.curselection():
        print(listbox.get(i))

def delete_selected_list_value():
    for i in listbox.curselection():
        print('deleted value: ', listbox.get(i))
        listbox.delete(i,i) # start is index of item to delete and end is also same as we want to delete only one item

def print_text_value():
    print(testvariable.get())

def clear_form():
    listbox.delete(0,END)
    testvariable.set('')

button1 = Button(text='get list value',command=print_list_values)
button1.pack()

button4 = Button(text='get selected list value',command=print_selected_list_value)
button4.pack()

button5 = Button(text='delete selected list value',command=delete_selected_list_value)
button5.pack()

button2 = Button(text='get text value',command=print_text_value)
button2.pack()

button3 = Button(text='clear all',command=clear_form)
button3.pack()

window.mainloop()