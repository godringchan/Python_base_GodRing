import tkinter
from tkinter import messagebox


def main():
    flag = False
    # 改变颜色和文字内容
    
    def change_lable_text():
        nonlocal flag
        flag = not flag
        (color, msg) = ("red", "hello,world!!!")\
            if flag else ("blue", "hello,python!!!")
        label.config(text=msg, fg=color)
        
    # 推出窗口的
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel("温情提示", "确定退出吗？"):
            top.quit()
    
    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry("240x160")
    # 窗口标题
    top.title("还好吗")
    # 创建标签对象，并添加到顶层窗口
    label = tkinter.Label(top, text="hello", font="Arial -32", fg="red")
    label.pack(expand=1) 
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象，指定添加到那个容器，通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text="修改", command=change_lable_text)
    button1.pack(side="left")
    button2 = tkinter.Button(panel, text="退出", command=confirm_to_quit)
    button2.pack(side="right")
    panel.pack(side="bottom")
    # 开启时间循环
    tkinter.mainloop()

if __name__ == "__main__":
    main()