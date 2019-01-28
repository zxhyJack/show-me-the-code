# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

import os
import re
from PIL import Image


def resize(file):
    img = Image.open(file)
    w, h = img.size
    print(w, h)
    img.resize((480, 720))
    print(img.size)
    # img.save('app/0005/test.jpg')


if __name__ == "__main__":
    # path = re.findall(r'*.jpg|png|jpeg', os.path.join('/home/mutou/'))
    # print(path)
    # resize('chenglong.jpg')
    resize('app/0005/test.jpg')
