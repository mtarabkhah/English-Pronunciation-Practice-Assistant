import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)



def talk(text):
    print(text)
    speaker.say(text)
    speaker.runAndWait()
    # with sr.Microphone() as source:
    #     listener.adjust_for_ambient_noise(source, duration = 1)

def compare(text1, text2):
    text1 = text1.lower().split()
    text2 = text2.lower().split()
    n = len(text1)
    count = 0
    diff = []
    for word in text1:
        word = ''.join(ch for ch in word if ch.isalnum())
        if word == '':
            n -= 1
            continue
        if word in text2:
            text2.remove(word)
            count += 1
        else:
            diff.append(word)
    score = count/n*100
    return score, diff

def assist(text):
    flag = True
    try:
        with sr.Microphone() as source:
            print(text)
            listener.adjust_for_ambient_noise(source, duration = 2)
            print('Listening...')
            voicecommand = listener.listen(source)
            textcommand = listener.recognize_google(voicecommand)
            # if 'stop' in textcommand.lower():
            #     return False
            talk(textcommand)
    except:
        pass
    return textcommand

file1 = open('SourceText.txt', 'r', encoding="utf8")
lines = file1.readlines()
for text1 in lines:
    if text1.strip() != '':
        text2 = assist(text1)
        score , diff = compare(text1,text2)
        if score<100:
            print(f'{round(score,2)}% accurate\nThese are the words you had missed')
            for word in diff:
                talk(word)
        else:
            print('Well done!')


# flag = False
# while flag:
#     flag = assist()