import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

def abc():
    pil_image = Image.open(r"E:\个人资料文件\秘密花园\甜菜玉\图\mmexport1564498974832.jpg")
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

# image11111 = abc()

# def xiaoyu_pic():
#     pil_image = Image.open(r"E:\个人资料文件\秘密花园\甜菜玉\图\mmexport1564498974832.jpg")
#     if pil_image.size[0]>500:
#         width = 500
#         height = int(pil_image.size[1] * (500/pil_image.size[0]))
#         pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
#     photo =  ImageTk.PhotoImage(pil_image)
#     return photo

# abc = xiaoyu_pic()


dict1= {"123":abc}

image11 = dict1["123"]()

tk_label = tk.Label(root, image=image11)

tk_label.pack()

root.mainloop()