import speech_recognition as sr
MyBot_ear = sr.Recognizer()

def MyBot_Listen_main():
    flag = False
    with sr.Microphone() as mic:       
        #Lọc tiếng môi trường trong 1s       
        MyBot_ear.adjust_for_ambient_noise(mic, duration = 0.5)  
        #Nghe trong 5s
        audio = MyBot_ear.record(mic, duration = 5)             
    print("MyBot: ...")
    try:   
        #Nhận diện = google, giọng "tiếng việt"
        you = MyBot_ear.recognize_google(audio, language= 'vi')   
    except sr.UnknownValueError:
        #Nếu không nhận diện được thì cho nhập
        flag = True
        you = str(input('NAT: '))                                 
    except sr.RequestError:                                         
        you = 'UNKNOWN'   
    if not flag:                                         
        print("NAT: " + you)
    return you
