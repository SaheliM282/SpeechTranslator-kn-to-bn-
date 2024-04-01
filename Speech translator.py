import googletrans
import playsound
import speech_recognition as sr
import gtts

recognizer = sr.Recognizer()
translator = googletrans.Translator()

with sr.Microphone() as source:
    intro = "স্বাগত, কন্নড় ভাষায় কিছু বলুন"
    print(intro)
    converted_audio = gtts.gTTS(intro, lang='bn')
    converted_audio.save("intro.mp3")
    playsound.playsound("intro.mp3")
    recognizer.adjust_for_ambient_noise(source)
    voice = recognizer.listen(source)

listen = recognizer.recognize_google(voice, language='kn')
translate = translator.translate(listen, dest='bn')
print("বাংলায় অনুবাদ: ", translate.text)
converted_audio = gtts.gTTS(translate.text, lang='bn')
converted_audio.save("translator.mp3")
playsound.playsound("translator.mp3")
