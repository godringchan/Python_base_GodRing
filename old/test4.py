import tkinter as tk
root = tk.Tk()
frame = tk.Label(root)
def callback(event):
    print('当前位置为：',event.width,event.height)
frame.bind('<Configure>',callback)
frame.pack()
tk.mainloop()