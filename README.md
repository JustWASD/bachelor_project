# CareHub
## Description

## Todo
* "while mood_update == 0" waiting sucks. Basically, I need to wait for the button input but I dont want to be stuck. Errors: If, while waiting for the button, messages are sent, all of the fire at once after the button press
* Security! Check the IDs and only answere if they are in the list of UserIDs we trust. Or something like that


### Todo from Mail
* Translate this whole message...
* Security: Ich werde das ganze über die Messanger ID lösen, die für jeden Telegram User einzigartig ist. Somit können nur Personen mit dem Bot interagieren, von denen die ID erlaubt wird.
* Zeitliche Events: Sprich, das automatische Umschalten der Bilder in der Bilderanzeige und das automatische auslösen einer Status Abfrage zu fixen Uhrzeiten den Tag über
* Viel Code clean-up: Mein ganzes Programm ist leider derzeit in einem file. Da bräuchte ich etwas hilfe, weil der erste Versuch es auf mehrere Files aufzuteilen war nicht erfolgreich... 
* Nice-To-Have-Feature: Die Möglichkeit Bilder an das Gerät zu schicken, damit sie in die Bilderrahmen Rotation aufgenommen werden. 
* Die UI ist noch nicht fertig. Sie ist funktional, aber schaut nicht gut aus zurzeit. Buttons sind an den richtigen Stellen, Schriften zu klein und so weiter. Das wird sehr viel spielerrei mit Tkinter und Testerei am 7" Display. 
* Hardware Tests, mit Mikrofon, Kamera und Lautsprecher zum testen wie der Videocall klingt und aussieht. Bis jetzt hab ich den Anruf nur gestartet und die Verbindung aufgebaut. Ich muss noch schauen wie das ganze klingt! 


## What's (kinda) working 
* /update opens a window with two buttons and closes after one button is pressed + it send info at the user. 
* /start
* multithreading tkinter and the telegram bot
* sending a message to a user with the telegram.bot
* opening and closing multiple tkinter windows in fullscreen
