
import random


class Dracon:

    def __init__(self):
        print("Drakon oyununa xow gelmisiniz..")
        self.name = input("Zehmet olmasa adinizi qeyd edin: ")
        print("Xow gelmisiniz",self.name)
        self.menu()


    def menu(self):
        print("""Salam siz bir magaraya teref gedirsiniz ve qarwiniza iki yol cixacaq
        iki yoldan birinde xow niyyetli ejdaha habsiki sizinle butun servetini bolecek
        digerinde acgoz ejdaha hansiki sizi yeyecek... Buyurun oyuna bawlayaq!
        """)



        self.drakon = random.randint(0,2)

        self.puan = 0
        print('Sizin 3 wansiniz var hansi yolla getmek isteyirsiniz secim edin')

        self.sans = 3
        for self.puan in range(3):
            self.secim = input("Secimizni: ")

            if self.secim == '1':
                if self.drakon == 1:
                    self.puan += 1
                    self.sans -=1
                    print("Men xow niyyetli ejdehayam, Sizin puana {} xal eleve olundu".format(self.puan))
                    print("Sizin  {} sansiniz qaldi".format(self.sans))

                else:
                    print("Men seni yedim")
                    break
            elif self.secim == '2':
                print("Man acmiwam sizi yedim")

                break
            else:
                print("Secim edin")



        if self.secim == self.drakon:
            self.puan = str(self.puan +1)
            print('Aferin siz {} defeye qalib oldunuz'.format(self.puan))

        if self.secim != self.drakon:
            self.drakon = str(self.drakon)
            print('Heyf siz meglub oldunuz men {} ejdaha idim'.format(self.drakon))









d = Dracon()