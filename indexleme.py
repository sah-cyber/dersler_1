
import datetime


def tedbir():
    name = input("Adinizi daxil edin: ")
    soname = input("Soyadinizi daxil edin: ")
    fazname = input("Ata adini daxil edin: ")
    britdayYou = int(input("Dogum ilinizi qeyd edin: "))
    whoYou = input("Cinsinizi daxil edin! (Bey yoxsa Xanim): ")

    today = datetime.date.today()
    year = today.year - britdayYou
    print("Sizin yasiniz", year)

    if year  <= 26:
        print("Sizin yasiniz 26 dan kicikdir !!! Tedbire giris icazeniz yoxdur")
        exit()
    elif whoYou.upper != "kisi" or whoYou.upper != "bey":
        print("Beylerden basqa wexslere girise izn yoxdur")
        exit()

    # elif whoYou.upper != "xanim" or whoYou.upper != "qadin":
    #     print("Xanimlardan basqa wexslere girise izn yoxdur")
    #     exit()

    else:
        print("Tedbire xos gelmisinzi!!!")

#tedbir()


def imtahan():
    print("Zehmet olmasa imtahan balinizi qeyd edin")
    fen_AnaDilin = int(input("Ana dili fendinden topladiginiz bali yazin: "))
    fen_Riaziyyat = int(input("Riaziyyat fendinden topladiginiz bali yazin: "))
    fen_Fizika = int(input("Fizika fendinden topladiginiz bali yazin: "))
    fen_Edebiyyat = int(input("Edebiyyat fendinden topladiginiz bali yazin: "))

    cem = (fen_AnaDilin+fen_Edebiyyat+fen_Fizika+fen_Riaziyyat)
    print('Sizin topladiginiz ball {}'.format(cem))
    if cem <60:
        print("Siz imtahandan kecid ede bilmediniz Teesuf olsun Sinifde qaldiniz!!")
    else:
        print("Sizi imtahandan ugurla kecdiniz!!")


#imtahan()


def elifba():
    name_list = []
    list_length = 3
    for i in range(list_length):
        name = input('Enter item to name: ')

        name_list.append(name)
        name_list.append(name[0])
        name_list.append(name[-1])
        name_list.sort()

    print('Elifba sirasi ile duzulus {}'.format(name_list))


    ind = name_list
    liste = []
    for a in ind:
        liste.append(ind.index(a))
    print('Indexlesme uzre {}'.format(liste))

elifba()

# dize = "xxyzzxax"
#
# liste = []
# for a in dize:
#   liste.append(dize.index(a))
# print(liste)












