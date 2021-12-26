from tkinter import *
import sqlite3

root = Tk()

root.title("Driver 2.0")
root.iconphoto(False, PhotoImage(file="images/qr-code-round.png"))
root.resizable(height=480, width=640)
root.resizable(False, False)

def show():
    connection = sqlite3.connect("database.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT oid, * FROM DRIVERS")
    res = cursor.fetchall()
    print(res)
    records = ""
    for ress in res: records += str(ress) + "\n"
    frame_0 = Label(root, text=records, padx=25, pady=20).grid(row=0, column=0, padx=25, pady=20)
    connection.close()

def del_entry():
    print(delete_entry.get())
    connection = sqlite3.connect("database.sqlite3")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM DRIVERS WHERE oid="+delete_entry.get())
    connection.commit()
    res = cursor.fetchall()
    print(res)
    records = ""
    for ress in res: records += str(ress) + "\n"
    frame_0 = Label(root, text=records, padx=25, pady=20).grid(row=0, column=0, padx=25, pady=20)
    connection.close()

initial_data="\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t"#"\n\t\t\t"


connection = sqlite3.connect("database.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT oid, * FROM DRIVERS")
res = cursor.fetchall()
print(res)
records = ""
for ress in res: records+=str(ress)+"\n"
frame_0 = Label(root, text=records, padx=25, pady=20).grid(row=0, column=0, padx=25, pady=20)
frame_1 = Label(root, text="Enter OID:", padx=25, pady=20).grid(row=1, column=0, padx=25, pady=20, sticky=W)

global delete_entry
delete_entry = Entry(root)
delete_entry.insert(0, string="")
delete_entry.grid(row=1, column=1, padx=25, pady=20, sticky=E+W, columnspan=2)

show_btn = Button(root, text="SHOW ALL", command=show).grid(row=0, column=1, padx=25, pady=20)
del_btn = Button(root, text="DELETE", command=del_entry).grid(row=1, column=2, padx=25, pady=20)
button_quit = Button(frame_0, text="EXIT", command=root.quit).grid(row= 2, column= 2, padx=25, pady=20)

root.mainloop()