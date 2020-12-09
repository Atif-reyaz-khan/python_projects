from gtts import gTTS
import os
f=open("Audiofile.txt","r")
myText=f.read().replace("\n"," ")
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save("output.mp3")
f.close()
os.system("start output.mp3")