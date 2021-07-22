from tkinter import *
from tkinter import messagebox
import pymysql


def addBook():

    def clear():
        book_id_entry.delete(0, END)
        book_title_entry.delete(0, END)
        book_author_entry.delete(0, END)
        book_amount_entry.delete(0, END)

    def addNewBookLogic():
        if book_id_entry.get() == "" or book_title_entry.get() == "" or book_author_entry.get() == "" or book_amount_entry.get() == "":
            messagebox.showerror("Error", "Please enter all the vaild details", parent=win)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="root1234", database="sys")
                cur = con.cursor()
                cur.execute("insert into book(id, book_title, book_author, stock) values(%s, %s, %s, %s)",
                            (book_id_entry.get(), book_title_entry.get(), book_author_entry.get(), book_amount_entry.get()))
                con.commit()
                messagebox.showinfo("Success", "New book added successfully!", parent=win)
                win.destroy()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)


    win = Tk()

    # app title
    win.title("Add a Book!")

    # Entry Book
    book_id_entry = Entry(win, width=25)
    book_id_entry.focus()
    book_id_entry.place(x=200, y=125)

    book_title_entry = Entry(win, width=25)
    book_title_entry.focus()
    book_title_entry.place(x=200, y=156)

    book_author_entry = Entry(win, width=25)
    book_author_entry.focus()
    book_author_entry.place(x=200, y=187)

    book_amount_entry = Entry(win, width=25)
    book_amount_entry.focus()
    book_amount_entry.place(x=200, y=218)

    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    # heading label
    heading = Label(win, text="Add A Book", font='Verdana 40 bold')
    heading.place(x=113, y=40)

    book_id = Label(win, text="Book ID:", font='Verdana 15 bold')
    book_id.place(x=60, y=130)

    book_title = Label(win, text="Book Title:", font='Verdana 15 bold')
    book_title.place(x=60, y=160)

    book_author = Label(win, text="Book Author:", font='Verdana 15 bold')
    book_author.place(x=60, y=190)

    book_amount = Label(win, text="Books in Stock:", font='Verdana 15 bold')
    book_amount.place(x=60, y=220)

    # Logic


    # button login and clear
    btn_login = Button(win, text="Add", font='Verdana 15 bold', command=addNewBookLogic)
    btn_login.place(x=170, y=265)

    btn_login = Button(win, text="Clear", font='Verdana 15 bold', command=clear)
    btn_login.place(x=265, y=265)

    win.mainloop()

