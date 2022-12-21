import pyttsx3
from playsound import playsound
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger

'''
update_trigger = OrTrigger([CronTrigger(hour=8, minute=30),
							CronTrigger(hour=12, minute=00),
							CronTrigger(hour=16, minute=30)])

def say_smth():
	print("I am working!")
	playsound("call_connecting_audio.wav")

def say_else():
	print("I am workin at specific times?!")


scheduler = BackgroundScheduler()
scheduler.add_job(say_smth, 'interval', minutes=10)
scheduler.add_job(say_else, update_trigger)
scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
	# This is here to simulate application activity (which keeps the main thread alive).
	while True:
		time.sleep(2)
except (KeyboardInterrupt, SystemExit):
	# Not strictly necessary if daemonic mode is enabled but should be done if possible
	scheduler.shutdown()

'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)     # setting up new voice rate

engine.say("bitte text eingeben. leeren text zum beenden")
engine.runAndWait()

run=True

while run==True:
	str = input("Ask user for something.")
	if (len(str)>1):
		engine.say(str)
		engine.save_to_file(str,str+".wav")
		engine.runAndWait()
else:
	run=False
