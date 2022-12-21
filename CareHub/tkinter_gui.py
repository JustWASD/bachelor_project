# Tkinter and Pillow
import time
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

# Standard
import threading
import cfg
#import browser_and_calling
from main import send_call_notification
import asyncio
from playsound import playsound
from apscheduler.schedulers.background import BackgroundScheduler


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

        for i in cfg.available_pictures:
            img = Image.open(i)
            img.thumbnail((screen_width, screen_height))
            img = ImageTk.PhotoImage(img)
            cfg.frame_pictures.append(img)

        frame_picture = Button(self.root, image=cfg.frame_pictures[0], command=self.draw_call)
        frame_picture.pack(fill=NONE, expand=True)

        tkinter_scheduler = BackgroundScheduler()
        tkinter_scheduler.add_job(lambda: self.change_bkg(frame_picture), 'interval', seconds=10)
        """Never close this mainloop"""
        self.root.mainloop()

    def change_bkg (self, frame_button):
        cfg.current_picture = cfg.current_picture + 1
        if cfg.current_picture == len(cfg.available_pictures):
            cfg.current_picture == 0
        frame_button.config(image=cfg.frame_pictures[cfg.current_picture])


    def draw_window_thread(self):
        update_window = Toplevel(self.root)
        update_window.title("CareHub")
        update_window.attributes("-fullscreen", True)
        update_window.focus_set()


        for i in cfg.icons:
            img = Image.open(i)
            img.resize((100, 100), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            cfg.tkinter_icons.append(img)

        my_font = font.Font(size=30, weight="bold")

        btn_happy = Button(update_window, width=15, image=cfg.tkinter_icons[0], text="Mir geht\n es gut!", compound=TOP, bg="#5cfac3",
                           font=my_font, command=lambda: self.clicked_happy(update_window))
        btn_sad = Button(update_window, width=15, image=cfg.tkinter_icons[1], text="Mir geht\n es nicht gut...", bg="#fa7070", compound=TOP,
                         font=my_font, command=lambda: self.clicked_sad(update_window))

        btn_happy.pack(side=RIGHT, fill=BOTH, expand=1, padx=5, pady=5)
        btn_sad.pack(side=LEFT, fill=BOTH, expand=1, padx=5, pady=5)

        return cfg.update_mood

    

    def draw_call(self):
       
        cfg.choose_user_to_call_windows = Toplevel(self.root)
        cfg.choose_user_to_call_windows.title("Video Telefonat")
        cfg.choose_user_to_call_windows.attributes("-fullscreen", True)
        cfg.choose_user_to_call_windows.config(bg="black")
        cfg.choose_user_to_call_windows.focus_set()
        my_font = font.Font(size=14, weight="bold")

        screen_width = cfg.choose_user_to_call_windows.winfo_screenwidth()
        screen_height = cfg.choose_user_to_call_windows.winfo_screenheight()

        for i in cfg.call_pictures:
            img = Image.open(i)
            img.thumbnail((int(screen_width / 2), int(screen_height / 2)))
            img = ImageTk.PhotoImage(img)
            cfg.call_icons.append(img)
        
        call_user1 = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4),
                            image=cfg.call_icons[1], text="Sabrina anrufen", compound=TOP,
                            font=my_font, command=lambda: self.call_user(1))
        call_user2 = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4),
                            image=cfg.call_icons[0], text="Gabriel anrufen", compound=TOP,
                            font=my_font, command=lambda: self.call_user(0))
        call_user3 = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4),
                            image=cfg.call_icons[2], text="Gruppe anrufen",
                            compound=TOP, font=my_font, command=lambda: self.call_user(2))
        close_button = Button(cfg.choose_user_to_call_windows, width=int(screen_width / 4), bg="#fa7070", text="Schließen",
                              command=cfg.choose_user_to_call_windows.destroy,
                              font=my_font)

        call_user1.pack(side=LEFT, fill=BOTH, expand=1)
        call_user2.pack(side=LEFT, fill=BOTH, expand=1)
        call_user3.pack(side=LEFT, fill=BOTH, expand=1)
        close_button.pack(side=LEFT, fill=BOTH, expand=1)

    def clicked_sad(self, update_window):
        print("Sad Button was clicked")
        cfg.update_mood = 2
        update_window.destroy()


    def clicked_happy(self, update_window):
        print("Happy Button was clicked")
        cfg.update_mood = 1
        update_window.destroy()



    def draw_wait_window(self):
        #TODO: Add voice and the picture.
        cfg.wait_for_connect_window = Toplevel(self.root)
        cfg.wait_for_connect_window.title("Anruf")
        cfg.wait_for_connect_window.attributes("-fullscreen", True)
        cfg.wait_for_connect_window.focus_set()

        cfg.wait_for_connect_window.config(bg="green")
        my_font = font.Font(size=14, weight="bold")

        cfg.waiting_label = Label(cfg.wait_for_connect_window, text="Bitte warten, Anruf wird aufgebaut", font=my_font, width=30)
        cfg.waiting_label.pack(fill=NONE, expand=True)


    #This function was originally in main but caused runtime errors (Tkinter GUI would freeze). I'm not sure if here
    # is the best place but it's currently working so whatever.
    def call_user(self, user_index):

        sent_call_notification = asyncio.run(send_call_notification(user_index))

        if sent_call_notification == 1:
            sent_call_notification = 0
            #browser_thread = threading.Thread(target=browser_and_calling.start_call, args=[user_index])
            #browser_thread.start()
            time.sleep(3)
            self.draw_wait_window()
            cfg.choose_user_to_call_windows.destroy()







