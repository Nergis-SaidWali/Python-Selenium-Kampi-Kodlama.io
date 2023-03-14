faiz=1.59
vade="36"
krediAdi="Ihtiyac Kredisi"

#print(vade+12) - error veren durum

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz= str(faiz)
print(type(faiz))

vade=36 #input("Lutfen istediginiz vade sayisini giriniz: ")
print(type(vade))
print(int(vade)+12) #type degisikligi icin birinci yontem

vade=36 #int(input("Lutfen istediginiz vade sayisini giriniz: ")) #type degisikligi icin ikinci yontem
print(type(vade))
print(vade+12)
vade=vade+12

#String interpolation
#sectiginiz vade sonucu ortaya cikan vade
print("sectiginiz vade sonucu ortaya cikan vade: "+str(vade))
print("sectiginiz vade sonucu ortaya cikan vade: {vadeSayisi}". format(vadeSayisi=vade))
print(f"sectiginiz vade sonucu ortaya cikan vade: {vade}")
#Ekrana sigdirma Alt+Z

isim="Halit" #input("isminizi giriniz")
metin= "Merhaba {Name}".format(Name=isim)
print(metin)

#f-string
metin= f"hosgeldinz {1+1}"
print(metin)

#listeler
#donguler
#fonksiyonlar

dizi = ["ihtiyac kredisi", 10, 5.2, True]
print(dizi)

krediler= ["Ihtiyac kredisi", "Tasit kredisi", "Konut kredisi"]
print(krediler)
print(type(krediler))
print(krediler[0])
# print(krediler[5]) -> index out of range error
 
print(len(krediler)) #length

krediler.append("Ozel kredi")
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop()
print(krediler)

krediler.pop(0) #index ile calisiyor, verdigimiz indexi siliyor
print(krediler)

krediler.remove("Tasit kredisi") #deger ile calisiyor, yazdigimiz degeri siliyor, index sirasina gore buldugu ilk elemani siler
print(krediler)

krediler.extend(["Y kredisi", "Z kredisi"]) #Tekrat array girip birden fazla eleman ekleyebiliyoruz
print(krediler)

# for
#i=0 i<10 i++

x=10
for i in range (x):
    print("xx")
    print(i)

print("*******************************")

for i in range(5,11):
    print(i)

print("*************************")

for i in range (0,51,10):
    print(i)

print("*******************")

#for i in range (0.1,0.5):
    #print(i)       -> float cannot be interpreted as an integer


krediler= ["Ihtiyac kredisi", "Tasit kredisi", "Konut kredisi"]

for kredi in krediler:
    print(kredi)

print("*************************")

for i in range(len(krediler)):
    print(krediler[i])

print("************************")

#CTLR+C sonsuz donguyu durdur
x=5
while(x<10):
    print("x")
    x+=1        # python'da i++ syntax yok
print("y")

print("**************************************")
while True:
    print("x")
    break

print("***********************")

i=0
while(i< len(krediler)):
    if krediler[i]=="Konut kredisi":
        break
    print(krediler[i])
    i+=1

    #Fonksiyonlar

    fiyat=100
    indirim=20
    yeniFiyat=fiyat-indirim

    #definition define - metod yazmak icin kullanilan keyword def

    def calculate():
        print(100-20)

    #void
    def calculateWithParams(fiyat, indirim):
        print(fiyat-indirim)

    def sayHello(name):
        print(f"Merhaba {name}")

    calculate()
    calculateWithParams(100,20)
    sayHello("Hamza")
    sayHello("Nergis")
    sayHello("Yusuf")
   

    def calculateAndReturn(price, discount):
        return price-discount
    
    yeniFiyat=calculateAndReturn(200,50)
    print(yeniFiyat)





