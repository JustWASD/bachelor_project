"""This file is used for config values, user IDs and the API token"""

APItoken= "****"

"""
Authorized Users:
177508822 = Sabrina [1]
927737771 = Gabriel [0]
-806449909 = Group Chat [2]
"""
user_id_list = [927737771, 177508822,-806449909]

'''
On Oct 27, 2022 [Multithread branch] I wrote some code that checks a folder for .jpg and .png. 
I could implement this again, to make adding pictures way easier and maybe even via the bot. 
But for now, you have to add pictures to the correct folder and add the name to the list. 
'''
available_pictures = ["/home/pi/projekt_test/CareHub/Images_and_Icons/frame_pic1.jpg",
                      "/home/pi/projekt_test/CareHub/Images_and_Icons/frame_pic2.jpg",
                      "/home/pi/projekt_test/CareHub/Images_and_Icons/frame_pic3.jpg",
                      "/home/pi/projekt_test/CareHub/Images_and_Icons/frame_pic4.jpg"]
frame_pictures = []
current_picture = 0

icons = ["/home/pi/projekt_test/CareHub/Images_and_Icons/happy_icon.png",
         "/home/pi/projekt_test/CareHub/Images_and_Icons/sad_icon.png"]
tkinter_icons = []

call_pictures = ["/home/pi/projekt_test/CareHub/Images_and_Icons/Gabs.jpg",
                 "/home/pi/projekt_test/CareHub/Images_and_Icons/Sabi.jpg",
                 "/home/pi/projekt_test/CareHub/Images_and_Icons/Gruppe.jpg"]
call_icons = []

# global Tkinter windows
# frame_picture = " "
wait_for_connect_window = " "
choose_user_to_call_windows = " "
waiting_label = " "

# generated url used by multiple sources
url = " "

#globals
update_mood = 0
call_connected = 0
