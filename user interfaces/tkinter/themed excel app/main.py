import tkinter as tk
from tkinter import ttk
import openpyxl


# tkinter --------------------------------
root = tk.Tk()

## setting the theme ---------------------
# enables us to apply ttk theme to our app
# we then say the parent is the root 
style = ttk.Style(root) 
root.tk.call('source','./forest-light.tcl')
root.tk.call('source','./forest-dark.tcl')
# style.theme_use('forest-light')
style.theme_use('forest-dark')


# functions -----------------------------

def load_excel_data():
    excel_file_path = './people.xlsx'
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active # we get the active sheet from the excel workbook
    # sheets thats currently open
    list_values = list(sheet.values) # list of tuples 
    # print(list_values)

    # set treeview heading
    for col_name in list_values[0]: # index 0 has header from excel sheet
        treeview.heading(col_name, text=col_name)

    # populate the values from index 1 to end in treeview
    for value_tuple in list_values[1:]:
        treeview.insert('',tk.END,values=value_tuple)
        # '' start at very start, till END to the tuple value

def insert_row_in_excel():
    print('inserted')
    # get information from the widgets 
    name = name_entry.get()
    age = int(age_spinbox.get())
    subscription_status = subscription_status_combobox.get()
    employment_status = 'employed' if employed.get() else 'unemployed'
    # print(name,age,subscription_status,employment_status) 

    # insert row in excel
    excel_file_path = './people.xlsx'
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active
    row_values = [name,age,subscription_status,employment_status]
    sheet.append(row_values)
    workbook.save(excel_file_path)

    # insert row in treeview
    treeview.insert('',tk.END,values=row_values)

    # clear form
    clear_form()

def toggle_mode():
    if mode_switch.instate(['selected']):
        style.theme_use('forest-light')
        # ttk.Style().theme_use('forest-light')
        # print('light')
    else:
        style.theme_use('forest-dark')
        # ttk.Style().theme_use('forest-dark')
        # print('dark')
    # print('mode toggled!')

def clear_form():
    name_entry.delete(0,'end')
    name_entry.insert(0,'Name')
    age_spinbox.delete(0,'end')
    age_spinbox.insert(0,'Age')
    subscription_status_combobox.set(combo_list[0])
    checkbutton.state(['!selected'])

# app name ---------------------
root.title('App Name')

# app icon ---------------------------
# https://www.pythontutorial.net/tkinter/tkinter-window/
root.iconbitmap('./favicon.ico')

# position the app window -----------------------------
# widthxheight±x±y
# https://www.pythontutorial.net/tkinter/tkinter-window/

# transparency -----------------------------
# https://www.pythontutorial.net/tkinter/tkinter-window/

# root.attributes('-alpha',0.5) # 50% transparency

# window stacking order -----------------------------
# https://www.pythontutorial.net/tkinter/tkinter-window/
# To ensure that a window is always at the top of the stacking order, 
# you can use the -topmost attribute

# root.attributes('-topmost', 1) # pin to top

# To move a window up or down of the stack, 
# you can use the lift() and lower() methods


# -----------------------------
frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text='Insert Row')
widgets_frame.grid(row=0,column=0,padx=20,pady=10)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0,'Name') # insert text at index 0

# on focus fire this event
# we here run a lambda, which is like a function which calls delete
# here we delete anything in the name_entry from index 0 to end of text 
name_entry.bind('<FocusIn>', lambda e: name_entry.delete('0','end'))
name_entry.grid(row=0,column=0,sticky='ew',padx=5,pady=(5,5)) # ew means east to west

age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
age_spinbox.insert(0,'Age')
age_spinbox.grid(row=1, column=0, sticky='ew',padx=5,pady=5)

combo_list = ['subscribed','not subscribed','other']
subscription_status_combobox = ttk.Combobox(widgets_frame,values=combo_list)
subscription_status_combobox.current(0)
subscription_status_combobox.grid(row=2, column=0, sticky='ew',padx=5,pady=5)

employed = tk.BooleanVar()
checkbutton = ttk.Checkbutton(widgets_frame, text='Employed',variable=employed)
checkbutton.grid(row=3,column=0,sticky='nsew',padx=5,pady=5) # north south east west

insert_button = ttk.Button(widgets_frame,text='Insert',command=insert_row_in_excel)
insert_button.grid(row=4,column=0,sticky='nsew',padx=5,pady=5)

seperator = ttk.Separator(widgets_frame)
seperator.grid(row=5,column=0,padx=(20,10), pady=10, sticky='ew')

# ==== ! DISABLED MODE SWITCH ======= issue with treeview expanding
# issue raised https://github.com/rdbende/Forest-ttk-theme/issues/8
# command links your widget to a certain function
# mode_switch = ttk.Checkbutton(widgets_frame,text='Mode',style='Switch', command=toggle_mode)
# mode_switch.grid(row=6,column=0,padx=5,pady=10,sticky='nsew')

# mode_switch = ttk.Checkbutton(root,text='Mode',style='Switch', command=toggle_mode)
# mode_switch.pack(padx=5,pady=5)

# -----------------------------

tree_frame = ttk.Frame(frame)
tree_frame.grid(row=0,column=1,pady=10)

# scrollbar needs to be added and attached to treeview
treescroll = ttk.Scrollbar(tree_frame)
treescroll.pack(side='right',fill='y') # fill entire vertical axis 

# treeview
excel_columns = ['name','age','subscription','employment']
# height : no of rows that i want to see at a time
treeview = ttk.Treeview(tree_frame,
                        show='headings',
                        columns=excel_columns, 
                        height=11, 
                        yscrollcommand=treescroll.set)

# setting individual column widths
treeview.column('name',width=100)
treeview.column('age',width=40)
treeview.column('subscription',width=100)
treeview.column('employment',width=100)

treeview.pack()
treescroll.config(command=treeview.yview) # this is what attaches the scroll to treeview

load_excel_data()

# -----------------------------

root.mainloop()