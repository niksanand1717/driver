from driver import Driver
import constants
from tkinter import *
import PIL.ImageTk as ImageTk
import PIL.Image as Image
from tkinter import messagebox
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, \
    CircleModuleDrawer, SquareModuleDrawer, GappedSquareModuleDrawer, QRModuleDrawer

from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask, HorizontalGradiantColorMask

root = Tk()
root.title("Driver 2.0")
root.iconphoto(False, PhotoImage(file="images/qr-code-round.png"))
root.resizable(height=480, width=640)
root.resizable(False, False)

global drivr
drivr = Driver(root)

# Functions

def clear():

    data_entered = Label(frame_1, text=initial_data)
    data_entered.grid(row=0, column=0, padx=25, pady=15, columnspan=4, rowspan=4)
    name_box.delete(0, END)
    phone_box.delete(0, END)
    address_box.delete(0, END)
    generate_button = Button(frame_1, text="GENERATE", state=DISABLED).grid(row=4, column=2, sticky=E)
    qr_code_initial = Label(frame_2, image=blank).grid(row=0, column=0, sticky=E+W)

def generate():
    qr = qrcode.QRCode(
        # error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=1,
        version=2
    )

    qr.add_data(data_to_show)
    qr.make(fit=True)
    img = qr.make_image(  # fill_color="black",
        # back_color="black",
        image_factory=StyledPilImage,
        color_mask=RadialGradiantColorMask(center_color=(255, 124, 0), edge_color=(0, 124, 255)),
        module_drawer=RoundedModuleDrawer())
    img.save("QR_Codes/demo2.png")
    # print("Generation Completed")
    # refresh_qr_code_button = Button(frame_2, text="REFRESH", command=refresh_qr_code).grid(row=1, column=0, sticky=E)
    # messagebox.showinfo("QR Code Status", "QR Code has been generated")
    img = ImageTk.PhotoImage(Image.open("QR_Codes/demo2.png"))
    qr_code_initial = Label(frame_2, image=img).grid(row=0, column=0, sticky=E+W)
    qr_code_initial.configure(image=img)
    qr_code_initial.image=img


def get_details():

    if name_box.get() == "":
        messagebox.showerror("Fill all the data", "fill the name")
        return
    drivr.name = name_box.get()
    if phone_box.get() == "":
        messagebox.showerror("Fill all the data", "fill the phone number")
        return
    drivr.phone_number = phone_box.get()
    if address_box.get() == "":
        messagebox.showerror("Fill all the data", "fill the address")
        return
    drivr.address = address_box.get()

    drivr.organisation = organisation.get()
    drivr.blood_group = bg.get()
    drivr.licence_expiry_month = month.get()
    drivr.licence_expiry_year = year.get()

    global data
    global data_to_show
    data_to_show = "\"name\":"+drivr.name+"\n\"phone\":"+drivr.phone_number+"\n\"address\":"+drivr.address+"\n\"organisation\":"+drivr.organisation+"\n\"blood_group\":"+drivr.blood_group+"\n\"month_validity\":"+str(drivr.licence_expiry_month)+"\n\"year_validity\":"+str(drivr.licence_expiry_year)
    data_entered = Label(frame_1, text="")
    data_entered = Label(frame_1, text=data_to_show)
    data_entered.grid(row=0, column=0, padx=25, pady=15, columnspan=4, rowspan=4)
    # print(name, phone, address, organisation_var, blood_group_var, month_validity, year_validity)
    clear_button = Button(frame_1, text="CLEAR", command=clear).grid(row=4, column=3, sticky=E+W)
    generate_button = Button(frame_1, text="GENERATE", command=generate).grid(row=4, column=2, sticky=E)
 

# constants
blood_groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
years = [x for x in range(2021, 2046)]
global bg
bg = StringVar()
bg.set("A+")
global month
month = StringVar()
month.set("Jan")
global year
year = IntVar()
year.set(years[0])
global organisation
organisation = StringVar()
organisation.set("GEHU")
global initial_data
initial_data="\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t\n\t\t\t"#"\n\t\t\t"
global blank
blank = ImageTk.PhotoImage(Image.open("images/Blank.jpg"))

# Frames
frame_0 = LabelFrame(root, text="Data Entry", padx=20, pady=25)
frame_0.grid(row=0, column=0, padx=25, pady=15)

frame_1 = LabelFrame(root, text="Entered Data", padx=20, pady=25)
frame_1.grid(row=0, column=1, padx=25, pady=15)

frame_2 = LabelFrame(root, text="QRCode", padx=20, pady=25)
frame_2.grid(row=0, column=2, padx=25, pady=15)

# Labels
name_label = Label(frame_0, text="Name:").grid(row=0, column=0, sticky=W)
phone_label = Label(frame_0, text="Phone Number:").grid(row=1, column=0, sticky=W)
address_label = Label(frame_0, text="Address:").grid(row=2, column=0, sticky=W)
organisation_label = Label(frame_0, text="Organisation:").grid(row=3, column=0, sticky=W)
blood_group_label = Label(frame_0, text="Blood Group:").grid(row=4, column=0, sticky=W)
license_validity = Label(frame_0, text="Licence Validity:").grid(row=5, column=0, sticky=W)

data_entered = Label(frame_1, text=initial_data)
data_entered.grid(row=0, column=0, padx=35, pady=25, columnspan=4, rowspan=4)

global qr_code_initial
qr_code_initial = Label(frame_2, image=blank).grid(row=0, column=0, sticky=E+W)


# Boxes (Entry Widgets)
name_box = Entry(frame_0)
name_box.insert(0, string="")
name_box.grid(row=0, column=1, sticky=E, columnspan=2)

phone_box = Entry(frame_0)
phone_box.insert(0, string="")
phone_box.grid(row=1, column=1, sticky=E, columnspan=2)

address_box = Entry(frame_0)
address_box.insert(0, string="")
address_box.grid(row=2, column=1, sticky=E, columnspan=2)


# Radio Buttons
Radiobutton(frame_0, text="GEHU", variable=organisation, value="GEHU").grid(row=3, column=1)
Radiobutton(frame_0, text="GEU", variable=organisation, value="GEU").grid(row=3 , column=2)


# CheckBoxes


# OptionMenu
blood_group_dropdown_menu = OptionMenu(frame_0, bg, *blood_groups).grid(row=4, column=1, columnspan=2, sticky=W+E)
validity_month_dropdown_menu = OptionMenu(frame_0, month, *months).grid(row=5, column=1, sticky=W+E)
validity_year_dropdown_menu = OptionMenu(frame_0, year, *years).grid(row=5, column=2, sticky=E+W)

# Buttons
save_details = Button(frame_0, text="SAVE", command=get_details).grid(row=10, column=1, pady=5, sticky=E+W, columnspan=1)
button_quit = Button(frame_0, text="EXIT", command=root.quit).grid(row= 10, column= 2, pady=5, sticky=E+W, columnspan=2)

generate_button = Button(frame_1, text="GENERATE", state=DISABLED).grid(row=4, column=2, sticky=E)
clear_button = Button(frame_1, text="CLEAR", state=DISABLED, command=clear).grid(row=4, column=3, sticky=E+W)

data = drivr.name+"\n"+drivr.phone_number+"\n"+drivr.address+"\n"+drivr.organisation+"\n"+drivr.blood_group

root.mainloop()