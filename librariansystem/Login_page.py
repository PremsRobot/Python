from Menu import *
import pymysql
from tkinter import messagebox
from tkinter import *
'''
LOGIN FUNCTION
'''
def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter Username And Password", parent=win)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="root1234", database="sys")
            cur = con.cursor()

            cur.execute("select * from librarian where librarian_name=%s and librarian_password=%s",
                        (user_name.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

            else:
                messagebox.showinfo("Success", "Successful Login", parent=win)
                close()  # close login window
                dashboard()  # calling menu
            con.close()  # close the connection of database
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)

# Clear function
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)

# Close function
def close():
    win.destroy()

'''
Login Window
'''
win = Tk()
# App title
win.title("Login!")
# Window size
win.maxsize(width=500, height=400)
win.minsize(width=500, height=400)
# Login Labels
heading = Label(win, text="Login", font='Verdana 40 bold')
heading.place(x=180, y=45)
username = Label(win, text="Username :", font='Verdana 15 bold')
username.place(x=60, y=160)
userpass = Label(win, text="Password :", font='Verdana 15 bold')
userpass.place(x=60, y=235)
# Entry boxes
user_name = StringVar()
password = StringVar()
userentry = Entry(win, width=30, textvariable=user_name, borderwidth=1, relief="solid", highlightcolor="green")
userentry.focus()
userentry.place(x=180, y=160)
passentry = Entry(win, width=30, show="*", textvariable=password, borderwidth=1, relief="solid", highlightcolor="cyan")
passentry.place(x=180, y=235)
# Login and Clear buttons
btn_login = Button(win, text="Login", font='Verdana 15 bold', command=login)
btn_login.place(x=165, y=310)
btn_login = Button(win, text="Clear", font='Verdana 15 bold', command=clear)
btn_login.place(x=275, y=310)
# Run window
win.mainloop()
