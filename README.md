# CareHub - most up to date branch: finalizing
## Description
[Coming Soon]

## Dependencies (WIP - list may not be complete)
* Python Telegram Bot Version 20.xx (https://github.com/python-telegram-bot/python-telegram-bot)
* Selenium Python (https://github.com/SeleniumHQ/selenium) 
* Tkinter (https://docs.python.org/3/library/tkinter.html)
* Pillow (https://pillow.readthedocs.io/en/stable/)
* Playsound (https://pypi.org/project/playsound/) + Linux needs GST (sudo apt install python3-gst-1.0)


## Setup (WIP)
### API Token
Generate a API Token by following the steps from the official Telegram Guide (https://core.telegram.org/bots)
### Users
To authorize a user you need to add the message_id to the list of authorized IDs. 
Send /start to the newly generated bot and you will find the message of the user on the console. 
### Pictures
Add all necessary pictures (pictures for the frame, user pictures and piktograms) to the folder and to the corresponding list (this will probably be changed in an future update)!
### Linux [WIP]
To make the UX as nice as possible, following settings must be taken into account: 
* unclutter -idle 0 
  This removes the mouse pointer
* Panel
  minimize when not in use. This hides the panel (aka Taskbar) when not in use. 
All these setting are necessary to have a full screen experience of the CareHub interface. 


## Todo
* Try-Catch for Network errors [Maybe not even necassary. More investigation needed.]
* Linux Interface: No taskbar, no mouse pointer, autostart of script. [WIP]


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
* Implemented a sheduler for calling an update during the day and changing the pictures in the frame.
* Progress of the whole project is approx.: 85%

