from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

my_font = " "

update_window = Tk()


happy_icon = Image.open("happy_icon.png")
happy_icon = happy_icon.resize((100, 100), Image.Resampling.LANCZOS)
#Convert the happy_icon to PhotoImage
happy_img= ImageTk.PhotoImage(happy_icon)

sad_icon = Image.open("sad_icon.png")
sad_icon = sad_icon.resize((100, 100), Image.Resampling.LANCZOS)
#Convert the happy_icon to PhotoImage
sad_img= ImageTk.PhotoImage(sad_icon)

my_font = font.Font(size = 40, weight = "bold")

update_window.title("CareHub")
update_window.attributes("-fullscreen", True)
update_window.focus_set()
btn_happy = Button(update_window,width=15, image=happy_img, text="I Am Happy!", compound= TOP, bg="#5cfac3", font=my_font, command=update_window.destroy)
btn_sad = Button(update_window, width=15, image=sad_img, text="I Am Sad!", bg="#fa7070", compound= TOP, font=my_font, command=update_window.destroy)

btn_happy.pack(side=RIGHT, fill=BOTH, expand=1, padx=5, pady=5)
btn_sad.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)

update_window.mainloop()