from speechToText import speechToTextReg
import kasa
import asyncio
import re
from multiCool import discoColorChangeFunc 


bulb = kasa.SmartBulb("10.0.0.136")
fanPlug = kasa.SmartPlug("10.0.0.60")
computerPlug = kasa.SmartPlug("10.0.0.232")

async def startProgram():
    error = False
    while error is False:
        try:
            await bulb.update()
            error = True
        except:
            pass
        error = False
        while error is False:
            try:
                await fanPlug.update()
                error = True
            except:
                pass
        error = False
        while error is False:
            try:
                await computerPlug.update()
                error = True
            except:
                pass

    
#     await bulb.update()
#     bulbToggle = await bulb.is_on()
#     fanToggle = await fanplug.is_on()
#     comToggle = await fanplug.is_on()

async def williamDoesSomething(input : str):
    if "william" in input or "volume" in input:
        #Turn Fan on or off
        if "fan" in input:
            if "on" in input and fanPlug.is_on == False:
                await fanPlug.turn_on()
            elif "off" in input and fanPlug.is_on == True:
                await fanPlug.turn_off()
        #Turn Computer charing on or off
        if "computer" in input and ("charge" in input or "charging" in input): 
            if "start" in input and computerPlug.is_on == False:
                await computerPlug.turn_on()
            elif "stop" in input and computerPlug.is_on == True:
                await computerPlug.turn_off()
        if "change" in input or "cancer" in input:
            #Change Brightness Levels
                if "brightness" in input:
                    numList = re.findall('\d+', input)
                    if len(numList) > 0:
                        brightnessLevel = int(numList[0])
                        if brightnessLevel <= 100:
                            await bulb.set_brightness(brightnessLevel)
            #Change Color 
                if "color" in input:
                    if "blue" in input:
                       await bulb.set_hsv(250, 100, 100) 
                    elif "red" in input:
                       await bulb.set_hsv(0, 100, 100)
                    elif "orange" in input:
                        await bulb.set_hsv(30, 100, 100)
                    elif "cyan" in input:
                        await bulb.set_hsv(200, 100, 100)
                    elif "green" in input:
                        await bulb.set_hsv(120, 100, 100)
                    elif"magenta" in input:
                        await bulb.set_hsv(300, 100, 100)
                    elif "yellow" in input:
                        await bulb.set_hsv(55, 100, 100)
                    elif "purple" in input:
                        await bulb.set_hsv(275, 100, 100)
                    elif "white" in input:
                        await bulb.set_color_temp(9000)
                if "temperature" in input:
                    numList = re.findall('\d+', input)
                    if len(numList) > 0:
                        brightnessLevel = int(numList[0])
                        if brightnessLevel <= 9000 and brightnessLevel >= 2500:
                            await bulb.set_color_temp(brightnessLevel) 
        if "disco" in input or "vsco" in input or "biscoe" in input:
            discoColorChangeFunc(input)
        #await bulb.update()
        # Turn light on or off
        if "bulb" in input or "light" in input:
            if "turn" in input:
                if "on" in input and bulb.is_on == False:
                    await bulb.turn_on()
                elif "off" in input and bulb.is_on == True:
                    await bulb.turn_off()

        error = False
        while error is False:
            try:
                await bulb.update()
                error = True
            except:
                pass


async def main():
    text = "idk"
    while True:
        await startProgram()
        text = speechToTextReg()
        print(text)
        await williamDoesSomething(text)
        if ("william" in text or "volume" in text) and ("exit" in text or "quit" in text):
            break

if __name__ == "__main__":
    #asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())
