import random
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, \
    CircleModuleDrawer, SquareModuleDrawer, GappedSquareModuleDrawer, QRModuleDrawer

from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask, HorizontalGradiantColorMask


mDrawers = [RoundedModuleDrawer(), CircleModuleDrawer(), SquareModuleDrawer(), GappedSquareModuleDrawer()]
cMasks = [RadialGradiantColorMask(), SquareGradiantColorMask(), HorizontalGradiantColorMask()]


def color_randomizer():
    color = ()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def generate(count):
    qr = qrcode.QRCode(
        # error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=1,
        version=2
    )

    filename = "QR_Codes/something"+str(count)+".png"
    print(filename)

    qr.add_data("Data\n\n\n\nData")
    qr.make(fit=True)
    if colormask == 
    img = qr.make_image(  # fill_color="black",
        # back_color="black",
        image_factory=StyledPilImage,
        color_mask=colormask,
        module_drawer=drawer)
    img.save(filename)
    # print("Generation Completed")
    # refresh_qr_code_button = Button(frame_2, text="REFRESH", command=refresh_qr_code).grid(row=1, column=0, sticky=E)
    # messagebox.showinfo("QR Code Status", "QR Code has been generated")
    # img = ImageTk.PhotoImage(Image.open("QR_Codes/"+filename+".png"))


count = 0
while input("Input: ") != '0':

    global drawer
    global colormask
    drawer = mDrawers[random.randint(0, 3)]
    colormask = cMasks[random.randint(0, 2)]
    count+=1
    generate(count)
