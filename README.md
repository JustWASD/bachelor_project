# CareHub - most up to date branch: finalizing
## Description

## Todo
* Implement a sheduler for calling an update during the day and change the pictures in the frame.
* Audio and more pictures for the Tkinter GUI. Add a synthezised voice to the wait_window. 
* "while mood_update == 0" waiting sucks. Basically, I need to wait for the button input but I dont want to be stuck. Errors: If, while waiting for the button, messages are sent, all of the fire at once after the button press

## Nice to haves...
* Adding pictures via the telegram bot
* Ability to initiate a call via the bot. 



## What's (kinda) working 
* /update opens a window with two buttons and closes after one button is pressed + it send info at the user. 
* /start
* multithreading tkinter and the telegram bot
* sending a message to a user with the telegram.bot
* opening and closing multiple tkinter windows in fullscreen
* simple security system
* having a screen inform the user that the call is being established

