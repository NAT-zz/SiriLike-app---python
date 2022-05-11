from gtts import gTTS
import os
import time
import playsound

def MyBot_Speak(audio):
    if(audio=="Unknown"):
        return
    tts = gTTS(text = audio, lang='vi') #Khởi tạo nội dung và ngôn ngữ 
    filename = 'voice.mp3'  #Tên và địng dạng File
    tts.save(filename)  #Lưu
    print("MyBot: " + audio)    
    playsound.playsound(filename)   #Chạy File âm thanh
    os.remove(filename) #Xóa File âm thanh

