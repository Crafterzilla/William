from os import system
from time import sleep
import datetime


system("./runVLC.sh")

while True:
    currentTime = datetime.datetime.now()
    minute = currentTime.strftime("%M")
    if int(minute) % 10 == 0:
        system("./runVLC.sh")
        sleep(60)
    sleep(1)
