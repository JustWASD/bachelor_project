from tkinter import *
from PIL import Image, ImageTk

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

screen_width = call_window.winfo_screenwidth()
screen_height = call_window.winfo_screenheight()

bild1.thumbnail((int(screen_width/2), int(screen_height/2)))
bild2.thumbnail((int(screen_width/2), int(screen_height/2)))
bild3.thumbnail((int(screen_width/2), int(screen_height/2)))


bild1 = ImageTk.PhotoImage(bild1)
bild2 = ImageTk.PhotoImage(bild2)
bild3 = ImageTk.PhotoImage(bild3)

btn1 = Button(call_window, image=bild1)
btn2 = Button(call_window, image=bild2)
btn3 = Button(call_window, image=bild3)
btn4 = Button(call_window, text="Close", command=call_window.destroy)

btn1.grid(row=3, column=1)
btn2.grid(row=3, column=3)
btn3.grid(row=3, column=5)

btn4.grid(row=3, column=7)

call_window.mainloop()