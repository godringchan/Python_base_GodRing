from tkinter import *  
import time

root = Tk()
root.title("My tools")
root.geometry('300x300+300+300')
def on_off():
   if btonoff['text'] == 'A':
      time.sleep(0.2)
      print('A have been finished!')
      btonoff['text'] = 'B'
   elif btonoff['text'] == 'B':
      time.sleep(0.2)
      print('B have been finished!')
      btonoff['text'] = 'C'
   else:
      time.sleep(0.2)
      print('Must be C! done !')
      btonoff['text'] = 'A'
btonoff = Button(root, text="A", command=on_off)
btonoff.place(x=100, y=160, width=100, height=40)
root.mainloop()