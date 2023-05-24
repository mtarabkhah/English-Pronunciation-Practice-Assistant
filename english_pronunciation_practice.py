import speech_recognition as sr
# Text-To-Speech: offline version
import pyttsx3
# Text-To-Speech: online version
from gtts import gTTS
from playsound import playsound
import os
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.tix import * # for Balloon


listener = sr.Recognizer()
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)

# Changing the text of a entry widget to a new text
def set_text(e,text):
    e.delete(1.0,END)  # Deleting previous text
    e.insert(1.0,text) # Setting new text
    # '1.0' is the position of the beginning of the text; This is the same as index '0' for Entry widgets
    # Other Example: '2.3' is the position before the fourth character of the second line.
    root.update() # While updating the text widgets in a loop, the window is not getting updated until the loop is running. 
                  # So, you won't see anything in the Tk window until the loop has completed.
                  # To avoid it 'freezing', you should update it periodically.

def set_label(e,text):
    e['text'] = text
    root.update()


def talk_online(e,text,accent,speed):
    set_text(e,text)
    tts = gTTS(text, lang='en', tld=accent, slow=speed)
    tts.save('tempvoice.mp3')
    playsound("tempvoice.mp3")
    os.remove("tempvoice.mp3")
    

def talk_offline(e,text,rate):
    set_text(e,text)
    speaker.setProperty("rate", rate)
    speaker.say(text)
    speaker.runAndWait()
    # with sr.Microphone() as source:
    #     listener.adjust_for_ambient_noise(source, duration = 1)

def talk(e,text):
    if TTSvalue.get() == 0:
        RATE = [100,150,200,250]
        talk_offline(e,text,RATE[speedvalue.get()])
    else:
        if speedvalue.get() == 1:
            slow = True
        else:
            slow = False

        ACCENTDICT = ['co.uk','us','ie','co.in']
        talk_online(e,text,ACCENTDICT[accentvalue.get()],slow)

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
            set_text(sourceText,text)
            listener.adjust_for_ambient_noise(source, duration = 2)
            set_label(informationLabel, 'Listening...')
            voicecommand = listener.listen(source)
            textcommand = listener.recognize_google(voicecommand)
            # textcommand = input("test!!! type instead of saying:")
            # if 'stop' in textcommand.lower():
            #     return False
            talk(recognizedText,textcommand)
            score, diff = compare(text,textcommand)
            if score<100:
                set_label(informationLabel,f'{round(score,2)}% accurate\nThis is the words you had missed')
                for word in diff:
                    talk(sourceText,word)
    except:
        pass
    return score, diff

# Clearing all the user input values
def clearButtonClick():
    set_text(sourceText,"")
    set_text(recognizedText,"")
    set_text(fileText,"")
    set_label(informationLabel,"")
    TTSvalue.set(0)
    speedvalue.set(0)
    accentvalue.set(0)
    assistvalue.set(0)
    veryslowradiobutton.configure(state = NORMAL)
    fastradiobutton.configure(state = NORMAL)
    Britishradiobutton.configure(state = DISABLED)
    Americanradiobutton.configure(state = DISABLED)
    Irishradiobutton.configure(state = DISABLED)
    Indianradiobutton.configure(state = DISABLED)

def startButtonClick():
    assistchoice = assistvalue.get()+1
    fileadd = fileText.get("1.0",END).strip('\n')
    if fileadd == '' : # Other conditions could be added
                       # like Checking the existance of a file
        set_label(informationLabel, "You should select the source file first")
        return
    file1 = open(fileadd, 'r', encoding="utf8")
    lines = file1.readlines()
    for text1 in lines:
        if text1.strip() != '':
            if assistchoice == 1:
                talk(sourceText,text1)
            else:
                score1, diff1 = assist(text1)                
                if score1<100:
                    if assistchoice == 3:
                        set_label(informationLabel, "Let's practice what you have miss-pronounced:")
                        for word in diff1:
                            score2 = score1
                            while score2 < 100:
                                score2, diff2 = assist(word)
                    elif assistchoice == 4:
                        set_label(informationLabel, "Let's try again:")
                        while score1<100:
                            score1, diff1 = assist(text1)
                else:
                    set_label(informationLabel,'Well done!')
    file1.close()

def TestButtonClick():
    talk(sourceText,"This is a sample text")

def fileButtonClick():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    set_text(fileText,filename)


def TTSselectionchange():
    if TTSvalue.get() == 1: # In case of online player "gTTS"
                            # The accent options are available so their radiobuttons should be ativated
                            # But, the only "Slow" and "Normal" speeds are available
                            # So, the other speed options should be deactivated
                            # Also, if "Very Slow" option was active, we will change it to "Slow"
                            # Similarly, if "Fast" option was active, we will change it to "Normal"
        veryslowradiobutton.configure(state = DISABLED)
        fastradiobutton.configure(state = DISABLED)
        Britishradiobutton.configure(state = NORMAL)
        Americanradiobutton.configure(state = NORMAL)
        Irishradiobutton.configure(state = NORMAL)
        Indianradiobutton.configure(state = NORMAL)
        if speedvalue.get() == 0:
            speedvalue.set(1)
        elif speedvalue.get() == 3:
            speedvalue.set(2)
    else:                   # In case of off-line player "pyttsx3"
                            # The accent options are not available so their radiobuttons should be deativated
                            # But, all the speeds are available
                            # So, "Very Slow" and "Fast" speed options should be activated
        veryslowradiobutton.configure(state = NORMAL)
        fastradiobutton.configure(state = NORMAL)
        Britishradiobutton.configure(state = DISABLED)
        Americanradiobutton.configure(state = DISABLED)
        Irishradiobutton.configure(state = DISABLED)
        Indianradiobutton.configure(state = DISABLED)

root = Tk()
root.title("English Pronounciation Practice")
root.geometry("650x300")

#Create a tooltip
tip = Balloon(root)

# Creating Lable Widgets
sourceLabel = Label(root,text="Source Text")
sourceLabel.place(x=5,y=5)
RecognizedLabel = Label(root,text="Recognized Text")
RecognizedLabel.place(x=5,y=60)
Label(root, text="Choose your player:", justify = LEFT).place(x=5,y=115)      # If you do not need to access/update any widgets later, you can skip assigning a variable name to it
Label(root, text="Choose player's speed:", justify = LEFT).place(x=5,y=140)
Label(root, text="Choose player's accent:", justify = LEFT).place(x=5,y=165)
Label(root, text="Choose desired assist:", justify = LEFT).place(x=5,y=190)
Label(root, text="Source File", justify = LEFT).place(x=5,y=215)
informationLabel = Label(root,text="",width=57,fg='red', borderwidth=2, relief="groove")
informationLabel.place(x=120,y=260)

# Creating Button Widgets
startButton = Button(root,text="start",command=startButtonClick,width=10)
startButton.place(x=550,y=5)
testButton = Button(root,text="Test Voice",command=TestButtonClick,width=10)
testButton.place(x=550,y=40)
clearButton = Button(root,text="Clear Form",command=clearButtonClick,width=10)
clearButton.place(x=550,y=75)
fileButton = Button(root,text="Select File",command=fileButtonClick,width=10)
fileButton.place(x=550,y=215)

# Creating Text Widgets
sourceText = Text(root,width=50,height = 3)
sourceText.place(x=120,y=5)
recognizedText = Text(root,width=50,height = 3)#,state=DISABLED)    # If you want to make the text widget, "read only"
                                                                    # Before and after inserting, change the state, otherwise it won't update
                                                                    # text.configure(state='normal')
                                                                    # text.insert('end', 'Some Text')
                                                                    # text.configure(state='disabled')
recognizedText.place(x=120,y=60)
fileText = Text(root,width=50,height = 1)
fileText.place(x=120,y=215)

# Creating RadioButton Widgets
TTSvalue = IntVar()
offlineradiobutton = Radiobutton(root, text="Offline", variable=TTSvalue, value=0,command=TTSselectionchange)
offlineradiobutton.place(x=140,y=115)
tip.bind_widget(offlineradiobutton,balloonmsg='Uses "pyttsx3" for Text to Speech conversion, You do not need to be connected to the internet')
onlineradiobutton = Radiobutton(root, text="Online", variable=TTSvalue, value=1,command=TTSselectionchange)
onlineradiobutton.place(x=220,y=115)
tip.bind_widget(onlineradiobutton,balloonmsg='Uses "gTTS" for Text to Speech conversion, You need to be connected to the internet')

speedvalue = IntVar()
veryslowradiobutton = Radiobutton(root, text="Very Slow", variable=speedvalue, value=0)
veryslowradiobutton.place(x=140,y=140)
slowradiobutton = Radiobutton(root, text="Slow", variable=speedvalue, value=1)
slowradiobutton.place(x=220,y=140)
normalradiobutton = Radiobutton(root, text="Normal", variable=speedvalue, value=2)
normalradiobutton.place(x=300,y=140)
fastradiobutton = Radiobutton(root, text="Fast", variable=speedvalue, value=3)
fastradiobutton.place(x=380,y=140)

accentvalue = IntVar()
Britishradiobutton = Radiobutton(root, text="British", variable=accentvalue, value=0,state= DISABLED)
Britishradiobutton.place(x=140,y=165)
Americanradiobutton = Radiobutton(root, text="American", variable=accentvalue, value=1,state= DISABLED)
Americanradiobutton.place(x=220,y=165)
Irishradiobutton = Radiobutton(root, text="Irish", variable=accentvalue, value=2,state= DISABLED)
Irishradiobutton.place(x=300,y=165)
Indianradiobutton = Radiobutton(root, text="Indian", variable=accentvalue, value=3,state= DISABLED)
Indianradiobutton.place(x=380,y=165)

assistvalue = IntVar()
Level1Radiobutton = Radiobutton(root, text="Level 1", variable=assistvalue, value=0)
Level1Radiobutton.place(x=140,y=190)
tip.bind_widget(Level1Radiobutton,balloonmsg="Assistant will read the whole text for you")
Level2Radiobutton = Radiobutton(root, text="Level 2", variable=assistvalue, value=1)
Level2Radiobutton.place(x=220,y=190)
tip.bind_widget(Level2Radiobutton,balloonmsg='''Assistant will show the text line by line for you to read,
then it shows the recognized text from your voice,
as well as the words you have mispronounced''')
Level3Radiobutton = Radiobutton(root, text="Level 3", variable=assistvalue, value=2)
Level3Radiobutton.place(x=300,y=190)
tip.bind_widget(Level3Radiobutton,balloonmsg='''Assistant will show the text line by line for you to read,
then it shows the recognized text from your voice,
as well as the words you have mispronounced.
It Asks you to repeat the mispronounced words until you pronounce them all correctly''')
Level4Radiobutton = Radiobutton(root, text="Level 4", variable=assistvalue, value=3)
Level4Radiobutton.place(x=380,y=190)
tip.bind_widget(Level4Radiobutton,balloonmsg='''Assistant will show the text line by line for you to read,
then it shows the recognized text from your voice,
as well as the words you have mispronounced.
It Asks you to read the text again until you pronounce it correctly''')

# Creating Ckeckbutton Widgets
# v5 = IntVar()
# v5.set(1)
# Checkbutton(root, text="Level 1", variable=v5).place(x=110,y=215)

root.mainloop()



# def setspeed():
#     print("How fast do you want to hear the voice")
#     speed = {1: ['Very Slow', 100],
#              2: ['Slow', 150],
#              3: ['Normal', 200],
#              4: ['Fast', 250]}
#     for key,value in speed.items():
#         print(f"{key}. {value[0]} -> Listen to sample voice")
#         speaker.setProperty("rate", value[1])
#         talk(sourceText,"This is a sample text")
        
#     speedchoice = int(input(f"Enter your choice (1~{key})"))
#     rate = speed[speedchoice][1]
#     return rate

# def setaccent():
#     # 'en-us': 'English (US)', 'en-ca': 'English (Canada)', 'en-uk': 'English (UK)', 'en-gb': 'English (UK)', 
#     # 'en-au': 'English (Australia)', 'en-gh': 'English (Ghana)', 'en-in': 'English (India)', 
#     # 'en-ie': 'English (Ireland)', 'en-nz': 'English (New Zealand)', 'en-ng': 'English (Nigeria)', 
#     # 'en-ph': 'English (Philippines)', 'en-za': 'English (South Africa)', 'en-tz': 'English (Tanzania)'
#     accentdict = {'1': ['UK', 'co.uk'],
#                   '2': ['US', 'us'],
#                   '3': ['Irish', 'ie'],
#                   '4': ['Indian', 'co.in']}
#     print("Which accent do you want to hear the voice")
#     for key,value in accentdict.items():
#         print(f"{key}. {value[0]} -> Listen to sample voice")
#         talk_online(f"{value[0]} accent: 'I often visit the ancient castle to admire its grandeur and pass through its imposing gates.'",value[1])
#     accentchoice = input(f"Enter your choice (1~{key})")
#     return accentdict[accentchoice][1]


# accent = setaccent()

# rate = setspeed()


# print("Available assist methods:")
# print("1. Listen to the whole text")
# print('''2. Try ro read each line of the text to check your pronounciation
#     and see what you have miss-pronounced''')
# print('''3. Try ro read each line of the text to check your pronounciation
#     and then try to correct what you have miss-pronounced''')
# print('''4. Try ro read each line of the text to check your pronounciation
#     and then try untill you have no have miss-pronounciation''')
# assistchoice = input("Select the assist you require (1~4): ")