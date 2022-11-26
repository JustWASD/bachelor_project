from threading import Thread
from tkinter import *
from PIL import Image, ImageTk

update_mood = 0

class TkinterWindow(Thread):

    # starts the thread
    def __init__(self):
        Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        # solves the error TCL_AsyncDelete
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("CareHub")
        self.root.attributes("-fullscreen", True)

        path = "testpic.jpg"

        img = ImageTk.PhotoImage(Image.open(path))

        # The Label widget is a standard Tkinter widget used to display a text or happy_icon on the screen.
        panel = Label(self.root, image=img)

        # The Pack geometry manager packs widgets in rows or columns.
        panel.pack(fill="none")
        self.root.mainloop()

    def draw_window_thread(self):
        update_window = Toplevel(self.root)
        update_window.title("CareHub")
        update_window.attributes("-fullscreen", True)
        update_window.focus_set()
        btn_happy = Button(update_window, text="Am Happy :)!", bg="#5cfac3", height=50, width=75,
                           command=lambda: self.clicked_happy(update_window))
        btn_happy.pack(side='right')

        btn_sad = Button(update_window, text="Am Sad :(!", bg="#fa7070", height=50, width=75,
                         command=lambda: self.clicked_sad(update_window, mood))
        btn_sad.pack(side='left')

        return mood

    def clicked_sad(self, update_window):

        print("Sad Button was clicked")
        mood = 2
        update_window.destroy()

    def clicked_happy(self, update_window):
        global update_mood
        print("Happy Button was clicked")
        update_mood = 1
        update_window.destroy()
