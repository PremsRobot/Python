from tkinter import *
import pymysql
import tkinter as tk

def display_book():
    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''


        def on_mousewheel(event):
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1
            if shift:
                canvas.xview_scroll(scroll, "units")
            else:
                canvas.yview_scroll(scroll, "units")


        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.bind_all("<MouseWheel>", on_mousewheel)



    def display_book_details(frame):
        '''Put in some fake data'''
        # Establish Connection
        con = pymysql.connect(host="localhost", user="root", password="root1234", database="sys")
        cur = con.cursor()
        cur.execute("select * from book")
        records = cur.fetchall()

        # Column Names
        column_names = ("Code", "Title", "Author", "Stock")

        # Empty List
        empty_list = []
        empty_list.append(column_names)

        # Creating Table
        for row in records:
            empty_list.append(row)
        print(empty_list)
        for i in range(len(empty_list)):
            if i == 0:
                for j in range(len(empty_list[0])):
                    e = Entry(frame, width=15, fg='blue', font=('Helvetica', 15, 'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, empty_list[i][j])
            else:
                for j in range(len(empty_list[0])):
                    e = Entry(frame, width=15, fg='green', font=('Helvetica', 15, 'bold'))
                    e.grid(row=i, column=j)
                    e.insert(END, empty_list[i][j])


    root = tk.Tk()
    canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
    frame = tk.Frame(canvas, background="#ffffff")
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((8, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    display_book_details(frame)

    root.mainloop()
