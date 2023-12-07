

words = {
    'kitab': 'book',
    'mawin': 'car',
    'qelem': 'pen',
    'karandaw':'pencil',
}


print ('=' * 15, 'Luget', '=' * 15)

help_message = """
s - Lugetde soz axtarmaq
a- yeni soz elave elemek
r- sozu silmek
k- lugetdeki sozleri ekrana cixartmaq
d- luegti ekrana cixartmaq
h- komek
q-cixiw

"""

chose = ""

while chose != 'q':
    chose = input("('h-komek')>> ")
    if chose.lower() == 's':
        word = input("Sozu yazin: ")
        res = words.get(word,'Bele soz yoxdur')
        print("{} sozun tercumesi {}".format(word,res))

    elif chose.lower() == 'a':
        word = input("sozu daxil edin: ")
        word_tercume = input("tercumeni daxil edin ")
        words[word]=word_tercume
        print("daxil etdiyiniz '{}' soz ve tercumesi '{}' elave olundu".format(word,word_tercume))

    elif chose.lower() == 'r':
        word = input("hansi sozu silmek isterdiniz?: ")
        del words[word]
        print('{} soz lugetden silindi'.format(word))

        # if word in words:
        #     print("sizin yazdiginiz {} soz lugetden silindi:".format(word))
        # else:
        #     print("{} sozu lugetde yoxdur".format(word))
    elif chose.lower() == 'k':
        for k in words:
            print(k)
        #print(words.keys())


    elif chose.lower() == 'd':
        for k,v in words.items():
            print(k,':',v)

    elif chose.lower() == 'h':
        print(help_message)



    elif chose.lower() == 'q':
        print("twk xidmet edirem sagolun ")
        break

    else:
        print("secim duzgun edin")