import speech_recognition as sr

# async def speechToText() -> str:
#     while True:
#         recognizer = sr.Recognizer()
#         recognizer.energy_threshold = 800
#         with sr.Microphone() as mic:
#                 print("Speak: ")
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#                 audio = recognizer.listen(mic, phrase_time_limit=5)
#                 try:
#                     text = recognizer.recognize_google(audio)
#                     text = text.lower()
#                     print("You said: {}".format(text))
#                     return text
#                 except:
#                     print("what did you say m8????")
#                     return "idk"
# def speechToTextReg() -> str:
#     while True:
#         recognizer = sr.Recognizer()
#         recognizer.energy_threshold = 800
#         with sr.Microphone() as mic:
#                 print("Speak: ")
#                 recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#                 audio = recognizer.listen(mic,timeout=8,phrase_time_limit=8)
#                 try:
#                     text = recognizer.recognize_google(audio)
#                     text = text.lower()
#                     print("You said: {}".format(text))
#                     return text
#                 except:
#                     print("what did you say m8????")
#                     return "idk"
def speechToTextReg() -> str:
	r = sr.Recognizer()
	#sr.dynamic_energy_threshold = False
	r.energy_threshold = 800
#	r.dynamic_energy_threshold = True
	text = ""
	try:
		with sr.Microphone() as mic:
			r.adjust_for_ambient_noise(mic, duration = 0.2)
			print("Say anything: ")
			audio = r.listen(mic, timeout=10, phrase_time_limit=10)
			print("Got audio")
			text = r.recognize_google(audio)
			text = text.lower()
			return text
			print("You said: {}".format(text))
			r = sr.Recognizer()
	except sr.UnknownValueError:
		r = sr.Recognizer()
		print("Sorry, I could not hear that")
		return "idk"
	except sr.WaitTimeoutError:
		r = sr.Recognizer()
		print("No sound ig")
		return "no sound"