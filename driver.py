from tkinter import *


class Driver:

    name = ""
    address = ""
    phone_number = ""
    organisation = ""
    blood_group = ""
    licence_expiry_month = ""
    licence_expiry_year = ""

    def __init__(self, root):
        name = StringVar(root)
        name.set("")
        address = StringVar(root)
        address.set("")
        phone_number = StringVar(root)
        phone_number.set("")
        organisation = StringVar(root)
        organisation.set("GEHU")
        blood_group = StringVar(root)
        blood_group.set("A+")
        licence_expiry_month = StringVar(root)
        licence_expiry_month.set("Jan")
        licence_expiry_year = IntVar(root)
        licence_expiry_year.set(2036)
