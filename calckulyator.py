print ("Kalkulyator proqramina xosh gelmisiniz!")

def toplama():
    reqem1 = int(input("Birinci reqemi daxil edin: "))
    reqem2 = int(input("Ikinci reqemi daxil edin: "))
    cem = reqem1+reqem2
    print(reqem1,"+",reqem2,"=", cem)

def cixma():
    reqem1 = int(input("Birinci reqemi daxil edin: "))
    reqem2 = int(input("Ikinci reqemi daxil edin: "))
    cem = reqem1-reqem2
    print(reqem1,"-",reqem2,"=", cem)

def bolme():
    reqem1 = int(input("Birinci reqemi daxil edin: "))
    reqem2 = int(input("Ikinci reqemi daxil edin: "))
    cem = reqem1/reqem2
    print(reqem1,"/",reqem2,"=", cem)

def vurma():
    reqem1 = int(input("Birinci reqemi daxil edin: "))
    reqem2 = int(input("Ikinci reqemi daxil edin: "))
    cem = reqem1*reqem2
    print(reqem1,"*",reqem2,"=", cem)


while True:
    print("""Menyuda reqemlerle emeliyat kecirmek isteyirsinizse  
    '+','-','/','*', duymelerini secin.
    Cixmaq isteyirsinizse 'q' duymesini davam etmek isteyirsinizse 
    Enter duymesini basin.""")


    menu = input("Emeliyati seciniz: ")

    try:
        if menu == 'q':
            print("Siz Cixdiniz Sagolun!!!")
            break

        elif menu == '':
            print("Bosluq olmaz")
        elif menu == '+':
            toplama()
        elif menu == '-':
            cixma()
        elif menu == '/':
            bolme()
        elif menu == '*':
            vurma()
        else:
            print("Reqem Seciniz.. ")
    except:
        print("Zehmet olmasa secim edin")

