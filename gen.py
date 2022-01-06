def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return text_width, text_height


def genPIC_Code(code, x, y, flip, thickness, size):
    import code128
    from PIL import Image, ImageFont, ImageDraw
    import os
    font_size = 32

    font = ImageFont.truetype("Roboto-Light.ttf", font_size)
    # Getting code generated and using saving it to 'data.png'
    a = code128.image(code, size, thickness)
    if os.path.exists('data'):
        a.save('data/code.png')
    else:
        os.mkdir('data')
        a.save('data/code.png')
    a.close()

    code_img = Image.open('data/code.png')
    ticketSample = Image.open('ticketTemplate.png')

    # rotation of code_img and adding numbers
    text_img = Image.new('RGB', (code_img.size[0], font_size))
    text_img.paste((255, 255, 255), [0, 0, text_img.size[0], text_img.size[1]])
    draw = ImageDraw.Draw(text_img)
    draw.text((0, 0), str(code), (0, 0, 0), font=font)
    text_img.save('temp.png')

    code_img_extended = Image.new('RGB', (code_img.size[0], code_img.size[1] + font_size))
    code_img_extended.paste((255, 255, 255), [0, 0, code_img_extended.size[0], code_img_extended.size[1]])
    code_img_extended.paste(code_img, (0, 0))
    text_pix_len = get_text_dimensions(str(code), font)[0]
    code_img_extended.paste(text_img, (
        round(code_img_extended.size[0] / 2 - text_pix_len / 2) - 2, code_img.size[1]))  # with insane offset
    code_img_extended.save('a.png')

    if flip:
        code_img_extended = code_img_extended.transpose(Image.ROTATE_90)

    # pasting a code_img to ticket and saving it
    x_size = x - round(code_img_extended.size[0] / 2)  # 183 is default value of x
    y_size = y - round(code_img_extended.size[1] / 2)  # 401 is default value of y
    ticketSample.paste(code_img_extended, (x_size, y_size))
    ticketSample.save('exit.png')
    code_img.close()
    ticketSample.close()
    code_img_extended.close()


def genPIC_TEXT(pic_dir, text, x, y):
    from PIL import Image, ImageFont, ImageDraw
    font_size = 40
    font = ImageFont.truetype("Roboto-Light.ttf", font_size)

    img_text = Image.new('RGB', (500, font_size + 1))
    img_text.paste((255, 255, 255), [0, 0, img_text.size[0], img_text.size[1]])
    draw = ImageDraw.Draw(img_text)
    draw.text((0, 0), str(text), (0, 0, 0), font=font)
    print(pic_dir)
    img_background = Image.open(pic_dir)
    img_exit = Image.new('RGB', img_background.size)
    img_exit.paste(img_background, (0, 0))
    img_exit.paste(img_text, (x, y - font_size))

    img_exit.save('exit.png')
    img_exit.close()
    # to do add text


def gen_identifier():
    import secrets
    import database
    records = database.get_records()
    if records is None:
        code = secrets.randbelow(10000000000000000000000)
    else:
        code = secrets.randbelow(10000000000000000000000)
        for i in range(len(records)):
            while int(records[i][0]) == code:
                code = secrets.randbelow(10000000000000000000000)
    return code
