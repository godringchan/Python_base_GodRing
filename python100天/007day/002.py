"""练习2：设计一个函数产生指定长度的验证码，
验证码由大小写字母和数字构成。"""

import random


def generate_code(code_len=4):
    random_code = ""
    all_chars = "123456789\
abcdefghijklmnopqrst\
ABCDEFGHIJKLMNOPQRST"
    # last_pos = len(all_chars) - 1
    for _ in range(code_len):
        random_code += random.choice(all_chars)
        # random_index = random.randint(0, last_pos)
        # random_code += all_chars[random_index]
    return random_code
random.shuffle()

if __name__ == "__main__":
    # len_ = int(input("验证码长度"))
    for _ in range(10):
        r_code = generate_code()
        print(r_code)