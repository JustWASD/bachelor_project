from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

my_font = " "

#1. Gabriel, 2. Sabi, 3. Placeholder
user_id = [927737771, 177508822, 203982093]


##sabi = Image.open("Sabi.jpg")
##gabs = Image.open("Gabs.jpg")
##dawg = Image.open("Dawg.jpg")

#bilder = [Image.open("Sabi.jpg"), Image.open("Gabs.jpg"), Image.open("Dawg.jpg")]
bild1 = Image.open("Sabi.jpg")
bild2 = Image.open("Gabs.jpg")
bild3 = Image.open("Dawg.jpg")




#for i in bilder:
 #   bilder = [ImageTk.PhotoImage(bilder)]


call_window = Tk()

call_window.title("Video Telefonat")
call_window.attributes("-fullscreen", True)
call_window.config(bg="black")
call_window.focus_set()

my_font = font.Font(size = 14, weight = "bold")

screen_width = call_window.winfo_screenwidth()
screen_height = call_window.winfo_screenheight()

bild1.thumbnail((int(screen_width/2), int(screen_height/2)))
bild2.thumbnail((int(screen_width/2), int(screen_height/2)))
bild3.thumbnail((int(screen_width/2), int(screen_height/2)))


bild1 = ImageTk.PhotoImage(bild1)
bild2 = ImageTk.PhotoImage(bild2)
bild3 = ImageTk.PhotoImage(bild3)

btn1 = Button(call_window,width=int(screen_width/4), image=bild1, text="Sabrina anrufen", compound= TOP, font=my_font)
btn2 = Button(call_window, width=int(screen_width/4), image=bild2, text="Gabriel anrufen", compound= TOP, font=my_font)
btn3 = Button(call_window, width=int(screen_width/4), image=bild3, text="Krankenschwester anrufen", compound= TOP, font=my_font)
btn4 = Button(call_window, width=int(screen_width/4), bg="#fa7070", text="Close", command=call_window.destroy, font=my_font)

btn1.pack(side=LEFT, fill=BOTH, expand=1)
btn2.pack(side=LEFT, fill=BOTH, expand=1)
btn3.pack(side=LEFT, fill=BOTH, expand=1)
btn4.pack(side=LEFT, fill=BOTH, expand=1)

call_window.mainloop()