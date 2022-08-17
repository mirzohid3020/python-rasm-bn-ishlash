"""
Pillow - bu pythonda rasmlar bilan ishlash kutubxonasi
pip install pillow
"""

# from PIL import Image
# im = Image.open('')
# angle = 90
# out = im.rotate(angle)
# out.show()

# from tkinter import *
# from PIL import ImageTk, Image
# root = Tk()
#
# rasm = Image.open('57cc4300035a6.jpg').resize((500, 200))
# NewImage = ImageTk.PhotoImage(rasm)
#
# label = Label(root, image=NewImage)
# label.pack()
#
#
# root.mainloop()


from tkinter import *
from PIL import ImageTk, Image

root = Tk()

rasm = Image.open('57cc4300035a6.jpg').resize((500, 200))
NewImage = ImageTk.PhotoImage(rasm)
rasm1 = Image.open('4159267.jpg').resize((500, 200))
NewImage1 = ImageTk.PhotoImage(rasm1)
rasm2 = Image.open('python-socket-programming.jpg').resize((500, 200))
NewImage2 = ImageTk.PhotoImage(rasm2)

def n():
    label.config(image=NewImage1)
    label1.config(image=NewImage2)

label = Label(root, image=NewImage)
label.pack()

label1 = Label(root, image=NewImage)
label1.pack()
btn = Button(root, text='click', bg='green', command=n)
btn.pack()

root.mainloop()



# from tkinter import *
# root = Tk()
# root.title('window')
# root.geometry('250x280')
# root.config(bg = 'grey')
# count = 0
# def d():
#     global count
#     count += 1
#     if count==34:
#         count = 0
#     # print(count)
#     bt.config(bg = 'green')
#
# bt = Button(root, text='🟪', width=7, height=3, bg='blue')
# bt.pack()
#
#
# root.mainloop()


