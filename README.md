This speech translator from Kannada to Bangla has been built on Python using PyCharm IDE. Four libraries - googletrans, playsound, speech_recognition and gtts have been used for translation directory for
Bangla and Kannada, audio, voice recognition and text-to-speech transformation respectively.
Target Group: It would help those Bengalis staying in Karnataka who do not know Kannada and want to know what people around them are talking about.
The voice and text assistance is in Bangla so that those who do not know English well can utilize the app. Complete voice assistance in the translator would help blind people as well.
[The translator is at the nascent stage and may further be improvised over time to broaden its horizon.]



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
