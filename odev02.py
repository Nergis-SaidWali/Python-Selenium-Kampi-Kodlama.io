print("Ogrenci kayit sistemine hosgeldiniz")

loop=True
students= ["Nergis Ulfet", "Hamza Ilyas", "Yusuf Said"]

def menu():
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n"
                "1 - Öğrenci Ekle\n"
                "2 - Öğrenci Sil\n"
                "3 - Öğrencileri Listele\n"
                "4 - Öğrenci Numarasi Öğrenme\n"
                "5 - Sistemi Kapat ! ")
    if sec == "1":
        print("Kayit ekleme menüsüne yönlendiriliyorsunuz.")
        print("-----------------------------------------------------------")
        addStudent()
    if sec == "2":
        print("Kayit Silme menüsüne yönlendiriliyorsunuz.")
        print("-----------------------------------------------------------")
        removeStudent()
    if sec == "3":
        print("Öğrenciler listeleniyor...")
        print("-----------------------------------------------------------")
        studentsList()
    if sec == "4":
        print("Öğrenci Numarasi öğrenme sayfasina gidiliyor...")
        print("-----------------------------------------------------------")
        studentNum()
    if sec == "5":
        print("Sistemden cikis yapiliyor....")
        print("-----------------------------------------------------------")
        exit()

def addStudent():
    print(students)
    add = input("Eklemek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    students.append(add)
    print(students)
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            addStudent()
        if sec == "2":
            menuReturn()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
        print("Lütfen geçerli bir seçenek giriniz.")
        cont()
    cont()

def removeStudent(): # COMPLETED
    print(students)
    remove = input("Silmek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    if remove in students:
        students.remove(remove)
    else:
        print("-----------------------------------------------------------")
        print("hatali giriş yaptiniz veri bulunamadi tekrar deneyin")
        print("-----------------------------------------------------------")
        removeStudent()
        print(students)
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            removeStudent()
        if sec == "2":
            menuReturn()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
    cont()

def studentsList():
    print(students)
    menuReturn()

def studentNum():
    print(students)
    num = input("Numrasini öğrenmek istediğiniz öğrencinin İsim ve soy ismini giriniz: \n ")
    stunum = students.index(num)
    print("{} Öğrencinin numarasi: {} ".format(num,stunum))
    def cont():
        print("-----------------------------------------------------------")
        sec = input("Daha fazla ekleme işlemi yapmak için --> 1\n"
                    "Devam etmek için -->2\n")
        if sec == "1":
            studentNum()
        if sec == "2":
            menuReturn()
        if sec not in ["1", "2"]:
            print("-----------------------------------------------------------")
            print("Lütfen geçerli bir seçenek giriniz.")
            cont()
            cont()

def menuReturn():
    print("-----------------------------------------------------------")
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz:\n"
                "1 - Ana menüye dön\n"
                "2 - Sistemi Kapat")
    if sec == "1":
        print("-----------------------------------------------------------")
        print("Ana menüye yönlendiriliyorsunuz.")
        menu()
    if sec == "2":
        print("-----------------------------------------------------------")
        print("Sistem kapaniyor....")
        exit()
    if sec not in ["1", "2"]:
        print("-----------------------------------------------------------")
        print("Lütfen geçerli bir seçenek giriniz.")
        menuReturn()

def exit():
    print("-----------------------------------------------------------")
    print("sistemden cisik yapiliyor.....")
    loop = False
    exit()

while loop:
    menu()

