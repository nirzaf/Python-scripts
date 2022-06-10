from tkinter import *

#label = an area widget that holds text and/or a image a window

window = Tk()
label = Label(window, text="Hello, world!")
label.place(x=100, y=100)

window.mainloop()