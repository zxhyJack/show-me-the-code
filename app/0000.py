from PIL import Image, ImageDraw, ImageFont


def add_num(path):
    img = Image.open(path).convert('RGB')
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype(
        '/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf', size=30)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-30, 0), '3', font=myfont, fill=fillcolor)
    img.save('result1.jpg', 'jpeg')

    return 0


def add_line(path):
    img = Image.open('cat.png').convert('RGB')
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype(
        '/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf', size=40)
    w, h = img.size
    draw.line((0, 0)+img.size, fill=125)
    draw.line((0, h, w, 0), fill="#ff0000")
    img.save('out.png', 'PNG')


if __name__ == '__main__':
    add_num('cat.png')
