from tkinter import Spinbox, LEFT, RIGHT
from tkinter.font import Font


def time_picker(Title):
    # Import Required Library
    import tkinter
    from tkcalendar import Calendar

    # Create Object
    root = tkinter.Tk()

    # Set geometry
    root.geometry("400x400")

    # Add Calendar
        #get date
    from datetime import datetime

    now = datetime.now()
    date = [int(now.strftime("%d")), int(now.strftime("%m")), int(now.strftime("%Y"))]

    # open calendar
    cal = Calendar(root, selectmode='day',
                   year=date[2], month=date[1],
                   day=date[0])

    cal.pack()

    # Add Button and Label
    hour = Spinbox(root, from_=0, to=23, width=5, state='readonly', font=Font(family='Helvetica', size=15))
    hour.place(x=125, y=200)

    minute = Spinbox(root, from_=0, to=60, width=5, state='readonly', font=Font(family='Helvetica', size=15))
    minute.place(x=200, y=200)

    def grad_date():
        date.config(text="Wybrana data to: " + cal.get_date())
        print(cal.get_date() + '|' + hour.get() + ':' + minute.get())
        file = open('temp.data', 'w')
        file.write(cal.get_date() + '|' + hour.get() + ':' + minute.get())
        root.destroy()
    tkinter.Button(root, text="Get Date",
                   command=grad_date).pack(pady=50)

    date = tkinter.Label(root, text="Wybierz date i godzinę", font=Font(family='Helvetica', size=14))
    date.pack()

    # Execute Tkinter
    root.mainloop()
