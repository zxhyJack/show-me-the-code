from PIL import Image, ImageDraw, ImageFont

def add_num(path):
    img = Image.open(path)
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    add_num('github-404.png')