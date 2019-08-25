import os

f_list = list()
def s_dir(dir1=os.curdir):
    # a = dir
    # print(dir1)
    b = os.listdir(dir1)
    print(b)
    for i in b:
        # print(i)
        c = os.path.join(dir1, i)
        # print(c)
        if os.path.isdir(c):
            s_dir(c)
        else:
            f_list.append(c)
    print(f_list)
    
if __name__ == "__main__":
    s_dir("D:\python_code\py_test\old")