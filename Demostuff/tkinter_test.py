from tkinter import *

window = Tk()
window.title("CareHub")
window.attributes("-fullscreen", True)

btn_happy = Button(window, text="Am Happy :)!", bg= "#5cfac3", height = 50, width = 75)
btn_happy.pack(side='right')

btn_sad = Button(window, text="Am Sad :(!", bg= "#fa7070", height = 50, width = 75)
btn_sad.pack(side='left')

window.mainloop()
