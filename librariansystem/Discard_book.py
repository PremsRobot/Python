from tkinter import *
from tkinter import messagebox
import pymysql

def discardBook():
    def clear():
        book_id_entry.delete(0, END)

    def getInfoLogic():
        if book_id_entry == "":
            messagebox.showerror("Error", "Please enter a book ID", parent=win)
        else:
            try:
                # Database Connection
                con = pymysql.connect(host="localhost", user="root", password="root1234", database="sys")
                cur = con.cursor()
                cur.execute("select * from book")
                records = cur.fetchall()

                # Display Details
                #topFrame = Frame(win)
                #topFrame.pack(side=TOP)
                for book in records:
                    if book[0] == int(book_id_entry.get()):
                        column_names = ("Code", "Title", "Author", "Stock", "Category")
                        for j in range(len(column_names)):
                            e = Entry(win, width=13, font=('Helvetica', 12, 'bold')).grid(row=4, column=j)

                            e.insert(162345, column_names[j])
                        for book_detail in range(len(book)):
                            e = Entry(win, width=13, font=('Helvetica', 12, 'bold')).grid(row=4, column=book_detail)
                            #e.
                            e.insert(250, book[book_detail])

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)


    # window creation
    win = Tk()

    # app title
    win.title("Discard a Book")

    # Entry Book
    book_id_entry= Entry(win, width=25).grid(row=1,column=2,columnspan=2)
    # book_id_entry.focus()
    # book_id_entry.place(x=200, y=125)

    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    # heading label
    heading = Label(win, text="Discard A Book", font='Verdana 40 bold').grid(row=0,column=0,columnspan=5)
    #heading.place(x=70, y=40)

    book_id = Label(win, text="Book ID:", font='Verdana 15 bold').grid(row=1,column=0,columnspan=3)
    #book_id.place(x=60, y=130)

    # Logic


    # Discard and Clear and Get Info Buttons
    btn_login = Button(win, text="Get Info", font='Verdana 15 bold', command=getInfoLogic).grid(row=3,column=1)
    #btn_login.place(x=205, y=205)

    btn_login = Button(win, text="Discard", font='Verdana 15 bold', command=None).grid(row=3,column=2)
    #btn_login.place(x=155, y=260)

    btn_login = Button(win, text="Clear", font='Verdana 15 bold', command=clear).grid(row=3,column=3)
    #btn_login.place(x=265, y=260)

    # Run Mainloop
    win.mainloop()
discardBook()
# Clear

