import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root) 
root.tk.call('source','./forest-light.tcl')
root.tk.call('source','./forest-dark.tcl')
style.theme_use('forest-dark')

def toggle_mode():
    if mode_switch.instate(['selected']):
        style.theme_use('forest-light')
    else:
        style.theme_use('forest-dark')

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text='Label Frame')
widgets_frame.grid(row=0,column=0,padx=20,pady=10)

mode_switch = ttk.Checkbutton(widgets_frame,text='Mode',style='Switch', command=toggle_mode)
mode_switch.grid(row=0,column=0,padx=5,pady=10,sticky='nsew')



tree_frame = ttk.Frame(frame)
tree_frame.grid(row=0,column=1,pady=10)

# scrollbar needs to be added and attached to treeview
treescroll = ttk.Scrollbar(tree_frame)
treescroll.pack(side='right',fill='y') # fill entire vertical axis 

# treeview
excel_columns = ['name','age','subscription','employment']

treeview = ttk.Treeview(tree_frame,
                        show='headings',
                        columns=excel_columns, 
                        height=11, 
                        yscrollcommand=treescroll.set)

treeview.column('name',width=100)
treeview.column('age',width=40)
treeview.column('subscription',width=100)
treeview.column('employment',width=100)

treeview.pack()
treescroll.config(command=treeview.yview) 


root.mainloop()