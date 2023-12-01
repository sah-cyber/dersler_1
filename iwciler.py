

class Iwciler():

    def __init__(self):
        self.name = []
        self.sorname = []
        self.job = []
        self.menu()

    def iwci(self):
        self.iwci_name = input("iwcinin adini qeyd edin: ")
        self.iwci_soname = input("iwcinin soyadini qeyd edin: ")
        self.iwci_job = input("iwcinin vezifesini qeyd edin: ")
        self.name.append(self.iwci_name)
        self.sorname.append(self.iwci_soname)
        self.job.append(self.iwci_job)
        print("iwci adin daxil edildi")
        melumat = "iwxi adi {}, soyadi {}, vezifesi {}"
        print(melumat.format(self.name,self.sorname,self.job))



    def siyahi(self):
        self.siyahi_goster()
        #for i in self.name:
            #print(i)

    #@classmethod
    def siyahi_goster(self):
        print("iwci adi {} ".format(self.name))
        print("iwci soyadi{} ".format(self.sorname))
        print("iwci vezifesi {} ".format(self.job))


    def menu(self):
        while True:
            print(""" Proqrama xow gelmisinzi
            1.iwcileri daxil edin 
            2. siyahini gosterin
            Q cixiw edin """)
            self.menu = input("seciminizi bildirin: ")

            if self.menu == '1':
                self.iwci()
            if self.menu == '2':
                self.siyahi()
            elif self.menu.upper() == 'Q':
                print("Cixdiniz..")
                exit()
            else:
                print("secim ediniz")






p1 = Iwciler()
