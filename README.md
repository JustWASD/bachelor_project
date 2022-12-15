# CareHub - most up to date branch: finalizing
## Description
[Coming Soon]

## Dependencies (WIP - list may not be complete)
* Python Telegram Bot Version 20.xx (https://github.com/python-telegram-bot/python-telegram-bot)
* Selenium Python (https://github.com/SeleniumHQ/selenium) 
* Tkinter (https://docs.python.org/3/library/tkinter.html)
* Pillow (https://pillow.readthedocs.io/en/stable/)

## Setup (WIP)
### API Token
Generate a API Token by following the steps from the official Telegram Guide (https://core.telegram.org/bots)
### Users
To authorize a user you need to add the message_id to the list of authorized IDs. 
Send /start to the newly generated bot and you will find the message of the user on the console. 
### Pictures
Add all necessary pictures (pictures for the frame, user pictures and piktograms) to the folder and to the corresponding list (this will probably be changed in an future update)!


## Todo
* Implement a sheduler for calling an update during the day and change the pictures in the frame.
* Add more folders and automated updating for icons and pictures
* Audio and more pictures/icons for the Tkinter GUI. 
* Add a synthezised voice to the wait_window. 
* "while mood_update == 0" waiting sucks. Basically, I need to wait for the button input but I dont want to be stuck. Errors: If, while waiting for the button, messages are sent, all of the fire at once after the button press

## Nice to haves...
* Adding pictures via the telegram bot
* Ability to initiate a call via the bot. 

## Progress  
* /update opens a window with two buttons and closes after one button is pressed + it send info at the user. (Tested)
* /start gives the user feedback and a quick tutorial on how to use the bot and commands. (Tested)
* multithreading tkinter, Selenium and the telegram bot (Tested)
* sending a message to a user with the telegram.bot (Tested)
* opening and closing multiple tkinter windows in fullscreen
* simple security system via message_ids
* having a screen inform the user that the call is being established
* Progress of the whole project is approx.: 85%

