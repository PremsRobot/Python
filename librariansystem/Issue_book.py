from tkinter import *

def clear():
    student_id_entry.delete(0, END)
    student_name_entry.delete(0, END)
    book_id_entry.delete(0, END)

win = Tk()

# app title
win.title("Library Management System!")

# Entry Book
student_id_entry = Entry(win, width=25)
student_id_entry.focus()
student_id_entry.place(x=200, y=125)

student_name_entry = Entry(win, width=25)
student_name_entry.focus()
student_name_entry.place(x=200, y=156)

book_id_entry = Entry(win, width=25)
book_id_entry.focus()
book_id_entry.place(x=200, y=187)

# window size
win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

# heading label
heading = Label(win, text="Issue A Book", font='Verdana 40 bold')
heading.place(x=95, y=40)

student_id = Label(win, text="Student ID:", font='Verdana 15 bold')
student_id.place(x=60, y=130)

student_name = Label(win, text="Student Name:", font='Verdana 15 bold')
student_name.place(x=60, y=160)

book_id = Label(win, text="Book ID:", font='Verdana 15 bold')
book_id.place(x=60, y=190)

# button login and clear
btn_login = Button(win, text="Issue", font='Verdana 15 bold', command=None)
btn_login.place(x=160, y=235)

btn_login = Button(win, text="Clear", font='Verdana 15 bold', command=clear)
btn_login.place(x=270, y=235)

win.mainloop()