import speech_recognition as sr

#definir el reconocedor

r =sr.Recognizer()

#definimos archivo de audio
audio_file = sr.AudioFile('good-afternoon.wav')

#speech reccognition
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio)

with open('result.txt', mode='w') as file:
    file.write("Texto destacado:")
    file.write("\n")
    file.write(result)
    print("Listo!")
