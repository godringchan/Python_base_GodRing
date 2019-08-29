# 练习3：设计一个函数返回给定文件名的后缀名
def get_suffix(file_name, has_dot=False):
    pos = file_name.rfind(".")
    if 0 < pos < len(file_name) - 1:
        index = pos if has_dot else pos + 1
        return file_name[index:]
    else:
        return None


if __name__ == "__main__":
    file_name = input("输入文件名")
    print(get_suffix(file_name, True))
