from time import sleep
from threading import Thread
import re
import asyncio
import kasa
from speechToText import speechToTextReg

bulb = kasa.SmartBulb("10.0.0.136")

input = ""

def getInput():
    global input
    while True:
        input = speechToTextReg()
        text = str(input)
        if ("william" in input or "volume" in input) and "stop" in text:
            break

def disco(speed : float):
    import io
    from contextlib import redirect_stdout

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    error = False
    while error is False:
        try:
            asyncio.get_event_loop().run_until_complete(bulb.update())
            error = True
        except:
            pass

    with io.StringIO() as buf, redirect_stdout(buf):
        print(bulb.hsv)
        output = buf.getvalue()

    numList = re.findall('\d+', output)
    changer = int(numList[0])
    global input
    input = ""

    while True:
        #print(changer)
        asyncio.get_event_loop().run_until_complete(bulb.set_hsv(changer, 100, 100))

        if changer == 360:
            changer = 0
        else:
            changer += 1
            
        if ("william" in input or "volume" in input) and "stop" in input:
            break
        sleep(speed)

def rgbDisco(speed : float):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    error = False
    while error is False:
        try:
            asyncio.get_event_loop().run_until_complete(bulb.update())
            error = True
        except:
            pass

    global input
    input = ""

    # blue: 250, red: 0, green: 120

    rgbColors = [250, 0, 120]
    
    index = 0

    while True:
        #print(index)
        asyncio.get_event_loop().run_until_complete(bulb.set_hsv(rgbColors[index], 100, 100, transition=0))

        if index == 2:
            index = 0
        else:
            index += 1
        if ("william" in input or "volume" in input) and "stop" in input:
            break
        sleep(speed)


def discoColorChangeFunc(input : str):
    print("start")
    speed = 0.1
    if "fast" in input:
        if "super" in input:
            speed = 0.01
        else:
            speed = 0.05
    elif "slow" in input:
        if "super" in input:
            speed = 0.2
        else:
            speed = 0.15

    t1 = Thread(target=disco, args=(speed,))
    if "rgb" in input or "rgv" in input:
        speed = 1
        if "fast" in input:
            if "super" in input:
                speed = 0.25
            else:
                speed = 0.5
        elif "slow" in input:
            if "super" in input:
                speed = 1.5
            else:
                speed = 1.25
        t1 = Thread(target=rgbDisco, args=(speed,))
    t2 = Thread(target=getInput)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("end")




