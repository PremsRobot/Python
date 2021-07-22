from tkinter import *
from tkinter import messagebox
import pymysql

def addLibrarian():
    def clear():
        new_librarian_entry.delete(0, END)
        new_librarian_password_entry.delete(0, END)


    def addNewLibrarianLogic():
        if new_librarian_entry.get() == "" or new_librarian_password_entry.get() == "":
            messagebox.showerror("Error", "Please enter all the vaild details", parent=win)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root1234", database="sys")
                cur = con.cursor()
                cur.execute("insert into librarian(librarian_name,librarian_password) values(%s,%s)",
                            (new_librarian_entry.get(), new_librarian_password_entry.get()))
                con.commit()
                messagebox.showinfo("Success", "New librarian added successfully!", parent=win)
                win.destroy()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)

    win = Tk()

    # app title
    win.title("Add a New Librarian!")

    # Entry Book
    new_librarian_entry = Entry(win, width=25)
    new_librarian_entry.focus()
    new_librarian_entry.place(x=300, y=130)

    new_librarian_password_entry = Entry(win, width=25)
    new_librarian_password_entry.place(x=300, y=160)

    # window size
    win.maxsize(width=700, height=500)
    win.minsize(width=700, height=500)

    # heading label
    heading = Label(win, text="Add New Librarian", font='Verdana 40 bold')
    heading.place(x=40, y=40)

    new_librarian = Label(win, text="Librarian Name:", font='Verdana 15 bold')
    new_librarian.place(x=40, y=130)

    new_librarian_id = Label(win, text="Librarian Password:", font='Verdana 15 bold')
    new_librarian_id.place(x=40, y=160)

    # button login and clear


    btn_login = Button(win, text="Add", font='Verdana 15 bold', command=addNewLibrarianLogic)
    btn_login.place(x=165, y=250)

    btn_login = Button(win, text="Clear", font='Verdana 15 bold', command=clear)
    btn_login.place(x=270, y=250)

    win.mainloop()

#addLibrarian()