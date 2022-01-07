from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x800")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=800,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"imgs/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=400, y=85,
    width=400,
    height=45)

img1 = PhotoImage(file=f"imgs/img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b1.place(
    x=400, y=221,
    width=400,
    height=45)

img2 = PhotoImage(file=f"imgs/img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b2.place(
    x=400, y=19,
    width=400,
    height=45)

img3 = PhotoImage(file=f"imgs/img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b3.place(
    x=400, y=153,
    width=400,
    height=45)

background_img = PhotoImage(file=f"imgs/background.png")
background = canvas.create_image(
    200.0, 400.0,
    image=background_img)

entry0_img = PhotoImage(file=f"imgs/img_textBox0.png")
entry0_bg = canvas.create_image(
    200.0, 176.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry0.place(
    x=11.0, y=156,
    width=378.0,
    height=38)

entry1_img = PhotoImage(file=f"imgs/img_textBox1.png")
entry1_bg = canvas.create_image(
    200.0, 108.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry1.place(
    x=11.0, y=88,
    width=378.0,
    height=38)

entry2_img = PhotoImage(file=f"imgs/img_textBox2.png")
entry2_bg = canvas.create_image(
    200.0, 244.0,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0)

entry2.place(
    x=11.0, y=224,
    width=378.0,
    height=38)

canvas.create_text(
    600.0, 784.5,
    text=" ",
    fill="#000000",
    font=("None", int(24.0)))

window.resizable(False, False)
window.mainloop()
