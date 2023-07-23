this is based off 

[Python Excel App - Excel Viewer & Data Entry Form [Tkinter, openpyxl] Python GUI Project](https://www.youtube.com/watch?v=8m4uDS_nyCk&ab_channel=CodeFirstwithHala)

## ttkthemes
https://medium.com/@fareedkhandev/themes-for-tkinter-232c17813e3a
https://www.reddit.com/r/Python/comments/lps11c/how_to_make_tkinter_look_modern_how_to_use_themes/

## notes
- tcl file is used to load the theme
- ttk is a package which is used to get the themed widgets of tkinter
- ttk allows us t omake our inter face look more modern

- python modules used
    - tkinter
    - openpyxl

- geometry managers of tkinter
    - pack
    - place
    - grid

- with grid layout by default everything is squished out
- we have to use padding with grid to add some spacing between the widgets

- various widgets that we are using
    - Frame
    - LabelFrame
    - Entry : text entry
    - SpinBox: age type entry
    - ComboBox
    - CheckBox
    - Button 
    - Separator
    - Checkbutton
    - Treeview
    - Scrollbar : works with Treeview

- to load excel data we are going to use what's called the tkinter tree view 
- we use openpyxl to interact with the excel file 