from datetime import date, datetime
import webbrowser as wb
import os 
import Speak
import time
import wikipedia as wkpd
from kanren import run, var, Relation, facts
from statistics import mode

#Danh sách việc cần làm
todo_list = ['DỌN PHÒNG', 'HỌC BÀI', 'TẬP THỂ DỤC']
#Chào 
def MyBot_Process_greeting():
    hour_now = datetime.now().hour
    if hour_now >= 5 and hour_now <= 12:
        return "Chào Buổi Sáng"
    elif hour_now > 12 and hour_now <= 19:
        return "Chào Buổi Chiều"
    else: 
        return "Chào Buổi Tối"

#Lấy thời gian hiện tại
def MyBot_Process_time():
    now = datetime.now()
    current_time = now.strftime("%H : %M : %S")
    return current_time

#Lấy ngày hiện tại
def MyBot_Process_day():
    today = datetime.today()
    current_day = today.strftime("%B %d, %Y")
    return current_day

#Tìm kiếm 
def MyBot_Process_search(platform):
    Speak.MyBot_Speak("Bạn Muốn Tìm Gì ?")
    keyword = str(input("NAT: "))
    if platform == 'google':
        url = f"https://www.google.com/search?q={keyword}"
    elif platform == 'youtube':
        url = f"https://www.youtube.com/search?q={keyword}"
    elif platform == 'địa điểm':
        url = f"https://www.google.nl/maps/place/{keyword}/&amp"
    elif platform == 'wikipedia':
        wkpd.set_lang("vi")
        Result = wkpd.summary(keyword, sentences=1)
        return Result
    elif platform == 'image':
        wkpd.set_lang("en")
        url = wkpd.page(f"{keyword}").images[0]
    wb.get().open(url)
    return keyword

#to-do list
def MyBot_Process_ToDoList(order):
    if(order == 'show'):
        tdl = ""
        for item in todo_list:
            tdl += item + " , "
        return tdl
    elif (order == 'add'):
        Speak.MyBot_Speak("Bạn Muốn Thêm Gì ?")
        keyword = str(input("NAT: ")).upper()
        todo_list.append(keyword)
        return keyword

#Note
def MyBot_Process_Note(order):
    if(order == 'add'):
        Speak.MyBot_Speak("Bạn Muốn Thêm Gì Vào Ghi Chú ? Vui Lòng Viết Không Dấu")
        keyword = str(input("NAT: "))
        Speak.MyBot_Speak("Hãy Đặt Tên Cho File Ghi Chú:")
        filename = str(input("NAT: "))

        with open(f"{filename}.txt", 'w') as f:
            f.write(keyword)
            f.close()
        return filename

#Chuẩn đoán theo triệu chứng
def MyBot_Process_Predicate(item):
    dis_pre = Relation() #Tạo quan hệ CHUANDOAN
    #Cài đặt Logic vị từ
    facts(dis_pre, ("ho","COVID-19"),("sốt","COVID-19"),("mệt mỏi","COVID-19"),("đau đầu","COVID-19"),("mất vị giác", "COVID-19"),("mất khứu giác", "COVID-19"),("đau họng", "COVID-19"),("ngạt mũi", "COVID-19"),("tiêu chảy", "COVID-19"), 
                    ("đầy bụng","Ung Thư Dạ Dày"),("khó tiêu","Ung Thư Dạ Dày"),("ăn không ngon","Ung Thư Dạ Dày"),("táo bón","Ung Thư Dạ Dày"),("sụt cân","Ung Thư Dạ Dày"),
                    ("tiêu chảy nhiều ngày","Ngộ Độc Thức Ăn"),("nôn ói nhiều ngày","Ngộ Độc Thức Ăn"),
                    ("đau bụng","Sốt Xuất Huyết"),("chảy máy cam","Sốt Xuất Huyết"),("tay chân lạnh","Sốt Xuất Huyết"),("đi ngoài ra máu","Sốt Xuất Huyết"),
                    ("sốt","Viêm Phổi"),("ho có đờm","Viêm Phổi"),("đau ngực","Viêm Phổi"),("khó thở","Viêm Phổi"),
                    ("cảm lạnh","Viêm Phế Quản"),("ho khan","Viêm Phế Quản"),
                    ("mệt mỏi","Viêm Gan"),("chán ăn","Viêm Gan"),("buồn nôn","Viêm Gan"),("sút cân","Viêm Gan"),("chóng mặt","Viêm Gan"),("suy giảm tuần hoàn","Viêm Gan")) 
    d = var()
    return run(0, d, dis_pre(item, d))          #Lấy tất cả kết quả của biểu thức Logic

#Tư vấn cách điều trị
def MyBot_Process_Cure(item):
    dis_cure = Relation() #Tạo quan hệ PHUONGPHAP
    #Cài dặt Logic vị từ
    facts(dis_cure, ("Viêm Phổi", "Uống Thuốc Ho"),
                    ("Viêm Phế Quản", "Luyện Tập Thở, Uống Thuốc Ho"),
                    ("COVID-19", "Dùng Vaccine Astrazeneca"),
                    ("Ung Thư Dạ Dày","Vô Phương Cứu Chữa"),
                    ("Ngộ Độc Thức Ăn","Ăn Chín Uống Sôi, Dùng Thuốc"),
                    ("Viêm Gan","Ăn Nhiều Hoa Quả, Kiêng Rượu Bia"))
    d = var()
    result = ''
    for item in run(0, d, dis_cure(item, d)):   #Lấy tất cả kết quả của biểu thức Logic
        result += item
    return result 

#Tìm kết quả có khả năng xảy ra cao nhất (trùng nhiều nhất)
def Find_MostDuplicate(x):
  return (mode(x))

#Chuẩn đoán bệnh
def MyBot_Process_DiseasePrediction():    
    Speak.MyBot_Speak("Hãy Nhập Các Triệu Chứng Của Bạn: ?")
    print("{Triệu Chứng}, {Triệu Chứng}, {...}")
    keyword = str(input("NAT: ")).lower()
    sym = keyword.split(", ")       #Tách trừng triệu chứng

    result_list = []
    for item in sym:
        result_list += MyBot_Process_Predicate(item) #Tập các bệnh giựa trên key
    result = Find_MostDuplicate(result_list)            #Tìm bệnh xuất hiện nhiều nhất

    return result
#Xử lí chính
def MyBot_Process_main(you):
    try:
        if you == "chào":
            MyBot_brain = "Xin Chào Bạn"
        elif 'hôm nay' in you:
            MyBot_brain = "Hôm Nay Là " + MyBot_Process_day()
        elif 'thời gian' in you:
            MyBot_brain = "Thời Gian Hiện Tại Là " + MyBot_Process_time()
        elif 'google' in you:
            MyBot_brain = "Đây Là Kết Quả Cho " + MyBot_Process_search('google') + " Trên Google"
        elif 'youtube' in you:
            MyBot_brain = "Đây Là Kết Quả Cho " + MyBot_Process_search('youtube') + " Trên Youtube"
        elif 'địa điểm' in you:
            MyBot_brain = "Đây Là " + MyBot_Process_search('địa điểm') + " Trên GoogleMap"
        elif 'wikipedia' in you:
            MyBot_brain = MyBot_Process_search('wikipedia')
        elif 'hình ảnh' in you:
            MyBot_brain = "Đây Là Hình Ảnh Cho " + MyBot_Process_search('image')
        elif 'thêm việc phải làm' in you:
            MyBot_brain = "Thêm '" + MyBot_Process_ToDoList('add') + "' Vào Việc Cần Làm Thành Công"
        elif 'việc phải làm' in you:
            MyBot_brain = "Đây Là Danh Sách Những Việc Cần Làm: " + MyBot_Process_ToDoList('show')
        elif 'thêm ghi chú' in you:
            MyBot_brain = "Thêm Ghi Chú Vào '" + MyBot_Process_Note('add') + "' Thành Công" 
        elif 'chuẩn đoán bệnh' in you:
            dis = MyBot_Process_DiseasePrediction()
            cur = MyBot_Process_Cure(dis)
            if dis == '':
                raise Exception
            else:   
                Speak.MyBot_Speak("Bệnh Của Bạn Có Thể Là: " + dis.upper()) 
                MyBot_brain =" Bạn Cần: " + cur
        else:
            raise Exception
    except:
        MyBot_brain = "Xin Lỗi Tôi Không Hiểu, Vui Lòng Thử Lại"
    print("MyBot: ...")
    time.sleep(0.5)
    return MyBot_brain
