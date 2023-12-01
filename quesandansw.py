
print("Sual-cavab oyununa xosh gelmisiniz...")

suallar = {'1.Quyruguna tava baglanmis it hansi suretde qacmalidir ki? tavanin sesi ewidilmesin?':'It yerinde dayanmalidir',
           '2.İnek uzunlugu on metr olan ipə bağlanmısdı, amma 200 m yol getdi. O buna nece nail oldu?':'İp hec bir yere baglanmamısdır',
           '3.On metrlik nerdivandan nece tullanmaq lazımdır ki, yıxılıb ezilmeyesen?': 'En asağı yerinden tullanmalısan',
           '4.Gozleriniz baglı olsa , ne gore bilersiniz?':'Yuxu',
           '5.Odda yanmaz, suda batmaz olan nedir?':'Buz',
           '6.Otuz iki doyuscunun bir komandiri var.':'Disler ve dil'}


bal = 0

for i,j in suallar.items():
    print(i)
    cavab = str(input("Sizin Cavabiniz: "))
    if cavab == j:
        print("Siz dogru cavab verdiniz))))")
        bal+= 10
        print("Sizin baliniz",bal)
    else:
        print("Sizin cavab sehfdir(((")
        bal -=10
        print("Sizin baliniz", bal)
