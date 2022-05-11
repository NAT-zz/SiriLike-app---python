import Listen, Process, Speak
Speak.MyBot_Speak(Process.MyBot_Process_greeting() + "! Tôi Có Thể Giúp Gì ?")  #Chào
while True:
    You_say = Listen.MyBot_Listen_main().lower()   #Nói 
    #You_say = str(input("NAT: ")).lower()           #Nhâp
    
    if 'tạm biệt' in You_say:
        Speak.MyBot_Speak("Tạm Biệt! Hẹn Gặp Lại ") #Kết thúc
        break
    else:
        MyBot_think = Process.MyBot_Process_main(You_say)   #Suy nghĩ
        Speak.MyBot_Speak(MyBot_think)                      #Trả lời