# CareHub V1.0 - The Project
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
1.) Send a /start command message to the BotFather (https://t.me/botfather) 
2.) send /newbot to the BotFather
3.) Give the bot a name and set a bot name -> CareHub with the botname CareHub_bot
4.) Save the newly generated API Token (very important!) 
5.) Insert the new API TOKEN into the cfg.py file.
Done. 

### Users
To authorize a user you need to add the message_id to the list of authorized IDs. 
Send /start to the newly generated bot and you will find the message of the user on the console. 
Insert the "user_id" into the list of User IDs in the cfg.py file. 

### Pictures
Add all necessary pictures (pictures for the frame, user pictures and piktograms) to the folder and to the corresponding list!
You can either overwrite the existing pictures or add new ones. 

### Linux [WIP]
To make the UX as nice as possible, following settings must be taken into account: 
* Install and add "unclutter -idle 0" to the Autostart Script (https://2021.jackbarber.co.uk/blog/2017-02-16-hide-raspberry-pi-mouse-cursor-in-raspbian-kiosk) 
  This removes the mouse pointer
* Panel Settings
  Check the option: "Minimize when not in use". This hides the panel (aka Taskbar) when not in use. 
* Add the carehub.system file in the follwing folder (https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-3-systemd)
  /etc/systemd/system/
  and then enter following commands: 
    sudo systemctl daemon-reload
    sudo systemctl enable carehub.service
    sudo reboot
  
  The Raspyberry should boot and then directly open the CareHub Interface. 
All these setting are necessary to have a full screen experience of the CareHub interface. 


## Nice to haves...
* Adding pictures via the telegram bot.
* Add new Users via a Password/Command without having to touch the sourcecode. 
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
* Progress of the whole project is approx.: 99% - is a project ever truly finished?
* V1.0 - The "Project Version" is done. 

