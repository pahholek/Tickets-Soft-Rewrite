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


New_Ticket(2, '$')


def Ticket_graphics():
    import gen
    import Date_Time
    Price = 69.0
    Price_Unit = '$'
    # gen code on picture
    gen.genPIC_Code(identifier, 183, 401, True, 4, 200)

    # Ticket Price Insert

    gen.genPIC_TEXT('exit.png', (str(Price) + Price_Unit), 1950, 235)

    # Issue Date insert
    from datetime import datetime

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    gen.genPIC_TEXT('exit.png', dt_string, 1950, 465)

    # Event Date Insert
    print(Date_Time.time_picker('PICK EVENT START DAY AND HOUR'))
    file = open('temp.data', 'r')
    lines = file.readlines()
    file.close()
    gen.genPIC_TEXT('exit.png', lines[0], 1950, 695)
