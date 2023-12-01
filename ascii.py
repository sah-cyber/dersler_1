while True:
    sozDaxilEt = input("Herfi daxil edin: ")

    try:
        if sozDaxilEt !=sozDaxilEt[0]:
            print("Bir soz daxil edin")
        print("Sizin Daxil etdiyiniz sozun ASCII kodu: ", ord(sozDaxilEt))

    except TypeError:
        print("Yalniz bir 'herf daxil edin' daxil edin")


