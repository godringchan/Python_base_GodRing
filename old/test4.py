import tkinter as tk 

root = tk.Tk()

# def change():
#     if text.get() == "开始运行":
#         text.set("取消运行")
#     else:
#         text.set("开始运行")

# text = tk.StringVar()
# button_01 = tk.Button(root, textvariable=text, command=change)
# text.set("开始运行")
# button_01.pack()
flag = tk.IntVar()
flag.set(1)
def change():
    if flag.get()==1:
        button1["text"]="停止运行"
        flag.set(2)
        # return change
    elif flag.get() == 2:
        button1["text"]="继续运行"
        flag.set(1)
        # return change
button1 = tk.Button(root, text="确认开始", command=change)
button1.pack()
# run_or_cancel_button()

root.mainloop()