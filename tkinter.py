from tkinter import *

#label = an area widget that holds text and/or a image a window

window = Tk()
label = Label(window, text="Hello, world!")
label.place(x=0, y=0)

window.mainloop()