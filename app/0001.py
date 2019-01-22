from PIL import Image, ImageDraw, ImageFont

def add_num(path):
    img = Image.open(path).convert('RGB')
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-30, 0), '3', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    add_num('github-404.png')