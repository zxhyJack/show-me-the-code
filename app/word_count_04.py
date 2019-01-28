# 任一个英文的纯文本文件，统计其中的单词出现的个数

import re


def count_word(file):
    lines = ''
    with open('app/0004.txt') as f:
        for line in f:
            lines += line.strip()

    lines = re.sub('\(|\)', '', lines)
    words = re.split(r'[;,.\s]\s*', lines)
    words.remove('')
    return len(words)


if __name__ == '__main__':
    num = count_word('app/0004.txt')
    print(num)
