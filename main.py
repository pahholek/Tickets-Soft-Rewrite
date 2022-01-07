


def combine(num):
    # import pillow to create blank page
    from PIL import Image
    image_on_page = 4
    # create blank Image
    combined_image = Image.new("RGB", (2480, 3508), (255, 255, 255))  # a4 size  2480 x 3508

    # checking number compatibility
    normal_loops = int(num / image_on_page)
    items_in_shorter_loop = num % image_on_page

    # normal_loop
    open_tickets = []
    for x in range(normal_loops):
        for i in range(image_on_page):
            # how to open image_on_page
            path = 'data/temp/images/' + str(x) + '/' + str(i) + '.png'
            open_tickets.append(Image.open(path))


# Create new ticket id, print_date, price, price_unit, used_date
def New_Ticket(Price, Price_Unit):
    import gen
    import time
    from datetime import datetime
    import Date_Time
    # get unique identifier
    identifier = gen.gen_identifier()
    print_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    Date_Time.time_picker('dupa')
    # add to database
    import database
    database.add_ticket(identifier, time.time(), Price, Price_Unit, 's')
    print(database.get_records)


def Ticket_graphics(Price, Price_Unit):
    import gen
    import Date_Time

    # gen code on picture
    gen.genPIC_Code(gen.gen_identifier(), 183, 401, True, 4, 200)

    # Ticket Price Insert

    gen.genPIC_TEXT('exit.png', (str(Price) + Price_Unit), 1950, 235)

    # Issue Date insert
    from datetime import datetime

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    gen.genPIC_TEXT('exit.png', dt_string, 1950, 465)

    # Event Date Insert
    # TODO: FIX THE RETURN
    Date_Time.time_picker('PICK EVENT START DAY AND HOUR')
    file = open('temp.data', 'r')
    lines = file.readlines()
    file.close()
    gen.genPIC_TEXT('exit.png', lines[0], 1950, 695)
    print('done')


def main():
    import tkinter
    import os
    import subprocess

    def btn_N_Normal():
        from PIL import Image
        New_Ticket(int(c_normalna_entry.get()), entry_j_monetarna.get())
        Ticket_graphics(int(c_normalna_entry.get()), entry_j_monetarna.get())

        # convert to pdf
        image1 = Image.open(r'exit.png')
        im1 = image1.convert('RGB')
        if not os.path.exists('temp'):
            os.mkdir('temp')
        im1.save(r'temp/temp.pdf')
        subprocess.check_call(['open', 'temp/temp.pdf'])


    def btn_clicked():
        print('a')

    window = tkinter.Tk()

    window.geometry("800x800")
    window.configure(bg="#ffffff")
    canvas = tkinter.Canvas(
        window,
        bg="#ffffff",
        height=800,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    img0 = tkinter.PhotoImage(file=f"imgs/img0.png")
    N_Normal = tkinter.Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_N_Normal,
        relief="flat")

    N_Normal.place(
        x=400, y=85,
        width=400,
        height=45)

    img1 = tkinter.PhotoImage(file=f"imgs/img1.png")
    Gen_PDF = tkinter.Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    Gen_PDF.place(
        x=400, y=221,
        width=400,
        height=45)

    img2 = tkinter.PhotoImage(file=f"imgs/img2.png")
    N_Ulgowy = tkinter.Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    N_Ulgowy.place(
        x=400, y=19,
        width=400,
        height=45)

    img3 = tkinter.PhotoImage(file=f"imgs/img3.png")
    Print_last_ticket = tkinter.Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    Print_last_ticket.place(
        x=400, y=153,
        width=400,
        height=45)

    background_img = tkinter.PhotoImage(file=f"imgs/background.png")
    background = canvas.create_image(
        200.0, 400.0,
        image=background_img)

    entry0_img = tkinter.PhotoImage(file=f"imgs/img_textBox0.png")
    entry0_bg = canvas.create_image(
        200.0, 176.0,
        image=entry0_img)

    c_normalna_entry = tkinter.Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0)

    c_normalna_entry.place(
        x=11.0, y=156,
        width=378.0,
        height=38)

    entry1_img = tkinter.PhotoImage(file=f"imgs/img_textBox1.png")
    entry1_bg = canvas.create_image(
        200.0, 108.0,
        image=entry1_img)

    entry_j_monetarna = tkinter.Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0)

    entry_j_monetarna.place(
        x=11.0, y=88,
        width=378.0,
        height=38)

    entry2_img = tkinter.PhotoImage(file=f"imgs/img_textBox2.png")
    entry2_bg = canvas.create_image(
        200.0, 244.0,
        image=entry2_img)

    c_ulgowa_entry = tkinter.Entry(
        bd=0,
        bg="#c4c4c4",
        highlightthickness=0)

    c_ulgowa_entry.place(
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


if __name__ == '__main__':
    main()
