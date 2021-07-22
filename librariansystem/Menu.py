from tkinter import *
from tkinter import messagebox
import pymysql
from Add_book import *
from Add_librarian import *
from Display_book import *
from Discard_book import *
from Update_password import *

# Dashboard function
def dashboard():
    das = Tk()

    '''
    LOGOUT FUNCTION
    '''
    def logout():
        messagebox.showinfo("Success", "You have logged out successfully!", parent=das)
        das.destroy()

    das.title("Menu")
    das.geometry("1000x750")

    # Menu buttons
    Button(das, text="Display Books", command=display_book, height=3, width=15, bg='#4a7abc').place(x=175, y=175)
    Button(das, text="Search Books", command=None, height=3, width=15, bg='#4a7abc').place(x=175, y=250)
    Button(das, text="Issue Books", command=None, height=3, width=15, bg='#4a7abc').place(x=175, y=325)
    Button(das, text="Return Books", command=None, height=3, width=15, bg='#4a7abc').place(x=175, y=400)
    Button(das, text="Add Books", command=addBook, height=3, width=15, bg='#4a7abc').place(x=175, y=475)
    Button(das, text="Discard Books", command=discardBook, height=3, width=15, bg='#4a7abc').place(x=675, y=175)
    Button(das, text="Overdue Books", command=None, height=3, width=15, bg='#4a7abc').place(x=675, y=250)
    Button(das, text="Add Librarians", command=addLibrarian, height=3, width=15, bg='#4a7abc').place(x=675, y=325)
    Button(das, text="Update Password", command=updatePassword, height=3, width=15, bg='#4a7abc').place(x=675, y=400)
    Button(das, text="Logout", command=logout, height=3, width=15, bg='#4a7abc').place(x=675, y=475)

