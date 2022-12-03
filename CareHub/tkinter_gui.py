# Tkinter and Pillow
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

# Standard
import threading
import cfg
from main import call_user


update_mood = 0


class TkinterWindow(threading.Thread):

    # starts the thread
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        # solves the error TCL_AsyncDelete
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("CareHub")
        self.root.attributes("-fullscreen", True)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        img = Image.open("Images_and_Icons/Nasi.jpg")
        img.thumbnail((screen_width, screen_height))

        img = ImageTk.PhotoImage(img)

        # The Label widget is a standard Tkinter widget used to display a text or happy_icon on the screen.
        picture = Button(self.root, image=img, command=self.draw_call)

        # The Pack geometry manager packs widgets in rows or columns.
        picture.pack(fill=BOTH)

        self.root.mainloop()

    def draw_window_thread(self):
        global update_mood

        update_window = Toplevel(self.root)
        update_window.title("CareHub")
        update_window.attributes("-fullscreen", True)
        update_window.focus_set()

        happy_icon = Image.open("Images_and_Icons/happy_icon.png")
        happy_icon = happy_icon.resize((100, 100), Image.LANCZOS)
        # Convert the happy_icon to PhotoImage
        happy_img = ImageTk.PhotoImage(happy_icon)

        sad_icon = Image.open("Images_and_Icons/sad_icon.png")
        sad_icon = sad_icon.resize((100, 100), Image.LANCZOS)
        # Convert the happy_icon to PhotoImage
        sad_img = ImageTk.PhotoImage(sad_icon)

        my_font = font.Font(size=40, weight="bold")

        btn_happy = Button(update_window, width=15, image=happy_img, text="I Am Happy!", compound=TOP, bg="#5cfac3",
                           font=my_font, command=lambda: self.clicked_happy(update_window))
        btn_sad = Button(update_window, width=15, image=sad_img, text="I Am Sad!", bg="#fa7070", compound=TOP,
                         font=my_font, command=lambda: self.clicked_sad(update_window))

        # Something about garbage collection... Doesnt work otherwise. Yey.
        btn_happy.image = happy_img
        btn_sad.image = sad_img

        btn_happy.pack(side=RIGHT, fill=BOTH, expand=1, padx=5, pady=5)
        btn_sad.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)

        return update_mood

    def draw_wait_window(self):
        cfg.choose_user_to_call_windows = Toplevel(self.root)
        cfg.choose_user_to_call_windows.title("Anruf")
        cfg.choose_user_to_call_windows.attributes("-fullscreen", True)
        cfg.choose_user_to_call_windows.focus_set()
        cfg.choose_user_to_call_windows.config(bg="green")
        label1 = Label(cfg.choose_user_to_call_windows, text="Bitte warten")
        label1.pack()

    def draw_call(self):
        bild1 = Image.open("Images_and_Icons/Sabi.jpg")
        bild2 = Image.open("Images_and_Icons/Gabs.jpg")
        bild3 = Image.open("Images_and_Icons/Dawg.jpg")

        cfg.choose_user_to_call_windows = Toplevel(self.root)
        cfg.choose_user_to_call_windows.title("Video Telefonat")
        cfg.choose_user_to_call_windows.attributes("-fullscreen", True)
        cfg.choose_user_to_call_windows.config(bg="black")
        cfg.choose_user_to_call_windows.focus_set()
        my_font = font.Font(size=14, weight="bold")

        screen_width = cfg.choose_user_to_call_windows.winfo_screenwidth()
        screen_height = cfg.choose_user_to_call_windows.winfo_screenheight()

        bild1.thumbnail((int(screen_width / 2), int(screen_height / 2)))
        bild2.thumbnail((int(screen_width / 2), int(screen_height / 2)))
        bild3.thumbnail((int(screen_width / 2), int(screen_height / 2)))

        bild1 = ImageTk.PhotoImage(bild1)
        bild2 = ImageTk.PhotoImage(bild2)
        bild3 = ImageTk.PhotoImage(bild3)

        call_user1 = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4),
                            image=bild1, text="Sabrina anrufen", compound=TOP,
                            font=my_font)
        call_user2 = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4),
                            image=bild2, text="Gabriel anrufen", compound=TOP,
                            font=my_font, command=lambda: call_user(2))
        call_user3 = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4),
                            image=bild3, text="Krankenschwester\nanrufen",
                            compound=TOP, font=my_font)
        close_button = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4), bg="#fa7070", text="Close",
                              command=cfg.choose_user_to_call_windows.destroy,
                              font=my_font)

        # Something about garbage collection... Doesnt work otherwise. Yey.
        call_user1.image = bild1
        call_user2.image = bild2
        call_user3.image = bild3

        call_user1.pack(side=LEFT, fill=BOTH, expand=1)
        call_user2.pack(side=LEFT, fill=BOTH, expand=1)
        call_user3.pack(side=LEFT, fill=BOTH, expand=1)
        close_button.pack(side=LEFT, fill=BOTH, expand=1)

    def clicked_sad(self, update_window):
        global update_mood
        print("Sad Button was clicked")
        update_mood = 2
        update_window.destroy()


    def clicked_happy(self, update_window):
        global update_mood
        print("Happy Button was clicked")
        update_mood = 1
        update_window.destroy()
