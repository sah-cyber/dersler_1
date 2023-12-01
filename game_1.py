import random
class Oyuncu:
    can = 6
    def __init__(self):
        self.name = input("Adiniz qeyd edin: ")
        if len(self.name) <=2:
            print("Zehmet olmasa qisa ad girmeyiniz ")
            return Oyuncu()
        else:

            cem = "Sizin adiniz {}, caniniz {} oyuna bawlaya bilersiniz"
            print(cem.format(self.name,self.can))
            self.menu()

    def menu(self):
        self.bas = input("Oyundan cixmaq isteyirsinizse Q duymesini basin, eks halda enter: ")
        if self.bas == 'q':
            print("cixdiniz...")
            exit()
        else:
            print('Xow geldiniz',self.name)
            self.run()



    def input_rand(self):

        try:
            self.first_number = int(input("ilk reqemi daxil edin: "))
            if self.first_number <= 0 or self.first_number >=10:
                print("Qeyd edilen reqem daxil edin")
                return  self.first_number
            else:
                self.second_number = int(input("ikinci reqemi daxil edin: "))
                if self.second_number <= 0 and self.second_number >10:
                    print("Qeyd edilen reqem daxil edin")
                    return self.second_number
        except:
            print("Sehf secim yeniden cehd edin")
            exit()
    def run(self):
        print("""Oyunun qaydasi Kampyter 1 reqem tutur siz bu reqemi tapmalisiniz""")
        print("Kampyt ucun 1-10 araliginda reqem seciniz : ")
        self.input_rand()
        self.number = random.randint(self.first_number, self.second_number)
        print("kampyterin reqem araliqlari {}--{} arasinda olacaq ve kampyter bu reqem araliginda bir reqem tutacaq".format(
                self.first_number,self.second_number))


        while True:
            self.secim = input("Bir reqem giriniz: ")
            if self.secim.isdigit():
                self.secim = int(self.secim)
                if self.number == self.secim:
                    print("Tebrikler siz qalib geldniz")
                    print("Kampyter {} reqemu tutmuwdur".format(self.number))
                    return  self.menu()

                elif self.number > self.secim:
                    print("Kampy tutdugu reqem sizin reqemden boyukdur")
                    self.can -=2
                    print("Sizin qalan caniniz: ",self.can)

                elif self.number < self.secim:
                    print("Kampy tutdugu reqem sizin reqemden kicikdir")
                    self.can-=2
                    print("Sizin qalan caniniz: ",self.can)


                if self.can == 0:
                    print("Siz meglub oldunuz suzin caniniz",self.can)
                    print("Kamyterin tutdugu reqem",self.number)
                    exit()


p1 = Oyuncu()

