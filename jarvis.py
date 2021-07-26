from re import search
from sys import prefix
from playsound import playsound 
from gtts import gTTS
from datetime import date, datetime
import random 
from random import choice
import webbrowser 
import time
import speech_recognition as sr
from pydub import AudioSegment
import os

r = sr.Recognizer()


def speeding():
    in_path = "Sora.mp3"
    ex_path = "speed.mp3"
    sound = AudioSegment.from_file(in_path)
    slower_sound = speed_swifter(sound, 1.3)
    slower_sound.export(ex_path, format="mp3") 

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate



def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask) 
        audio = r.listen(source)
        voice =""
        try:
            voice = r.recognize_google(audio , language="tr-TR")              
        except sr.UnknownValueError:
            speak("Anlayamadım efendim, lütfen tekrar edin")
        except sr.RequestError:
            speak("Efendim sistem çalışmıyor")
        return voice 

def response(voice):
    if "sora" in voice:
        speak("buyrun efendim")
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Sunday":
            today = "Pazar"

        elif today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"          

        elif today == "Saturday":
            today = "Cumartesi"  

        speak(today)          

    if 'günaydın' in voice: 
        speak('nasıl hizmet edebilirim efendim') 
    if 'saati söyler misin' in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime('%H:%M:%S')    
        selection = random.choice(selection)
        speak(selection + clock)

    if "google'da arama yap" in voice:
        search = record ('Sora: NEYİ ARAŞTIRMAK İSTİYORSUNUZ')    
        url = 'https://www.google.com/search?q='+search
        webbrowser.get().open(url)
        speak(' buyrun efendim')
    if "youtube'da arama yap" in voice:
        search = record ('Sora: NEYİ ARAŞTIRMAK İSTİYORSUNUZ')
        url = "https://www.youtube.com/search?q="+search
        webbrowser.get().open(url)
        speak(search + " buyrun efendim")
    if 'teşekkürler' in voice:
        speak('ne demek efendim size hizmet etmek benim için bir zevk')    
    if 'tamam kapatabilirsin' in voice or "kapatabilirsin" in voice:
        speak('kendinize iyi bakın efendim')
        exit() 
    if "20 saniye bekle" in voice:
        speak("20 saniye bekliyorum")
        time.sleep(20)
        speak("dinliyorum efendim")      
    if "10 saniye bekle" in voice:
        speak("10 saniye bekliyorum")
        time.sleep(10)
        speak("dinliyorum efendim")
    if "30 saniye bekle" in voice:
        speak("30 saniye bekliyorum.")
        time.sleep(30)
        speak("dinliyorum efendim")    
    if "1 dakika bekle" in voice:
        speak("1 dakika bekliyorum")
        time.sleep(60) 
        speak("dinliyorum efendim")  
    if "2 dakika bekle" in voice:
        speak("2 dakika bekliyorum")
        time.sleep(120)
        speak("dinliyorum efendim") 
    if "3 dakika bekle" in voice:
        speak("3 dakika bekliyorum")          
        time.sleep(180)
        speak("dinliyorum efendim")
    if "5 dakika bekle" in voice:
        speak("5 dakika bekliyorum")
        time.sleep(300)
        speak("dinliyorum efendim")




def speak(string):
    tts = gTTS(text=string, lang='tr', slow=False) 
    file = "Sora.mp3"
    tts.save(file)
    speeding()
    playsound("speed.mp3")
    os.remove(file)
    os.remove("speed.mp3")

speak("Hoş Geldiniz Efendim!")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)


    
