import string
import random

# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券
def generate_verification(number, length):
    '''
    number: 数量
    length: 长度
    '''
    source = list(string.ascii_uppercase)
    source.extend(map(str, list(range(0, 10))))
    verification_code = set()
    while(len(verification_code) <= number):
        code = ''
        while len(code) < length:
            code += random.choice(source)
            # code += source[random.randint(0, 35)]
        verification_code.add(code)
    return verification_code


if __name__ == '__main__':
    verifications = generate_verification(10, 10)
    print(verifications)
