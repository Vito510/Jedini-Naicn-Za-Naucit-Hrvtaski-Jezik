


try:
    import sys
    import random
    import re
except:
    print("Nedostaju neki ili svi library \nError: PEN15")
    x = input("Klikni ENter da se ugasi čudo")
    exit()

line = ""
clean = ""
user = ""
upit = ""

tocno = int(0)
netocno = int(0)

#test

sys.setrecursionlimit(15000)

def GetLineCount(filepath):

    linecount = int(0)

    for line in open(filepath, "r", encoding="UTF-8"):
        linecount = linecount + 1

    return linecount+1

def cleaning(user_in):

    clean_list = ['č','ć','Č','Ć']
    clean = user_in

    for i in clean_list:
        try:
            clean = clean.replace(i,'c')
        except:
            meko()
            break

    return clean

def meko():

    if int(diff) < 3:
        filepath = 'src/Razvrstaj_'+diff+'.txt'
    else:
       filepath = 'src/Razvrstaj_3.txt'

    if random.randint(1,Fake_Chance) == 1:

        if int(diff) < 3:
            filepath = 'src/Sve_'+diff+'_c.txt'
        else:
            filepath = 'src/Sve_3_c.txt'


    


    upit = None
    while upit == None:
        if upit == None:
            print("None")

        fp = open(filepath, "r", encoding="UTF-8")
        ran = random.randint(1,GetLineCount(filepath))

        for i, line in enumerate(fp):
            if i == ran:

                upit = line
                return upit
                break


    fp.close()   


print('Sve riječi izvučene su iz databaze Hrvatskog jezičnog portala.\nU toj databazi postoji 73284 riječi koje sadrže slovo Č i 26491 riječi koje sadrže slovo Ć\n\n Izvukao i programirao "Dr." "Prof." Vito Čuić\n E da i definitivno nisam i neću provijeriti jesu li točno napisane u databazi\n')


print("Odabir težine: \n 1) Lagano \n 2) Normalan lik \n 3) Teško \n 4) Profesor \n\n 0) POMOĆ nemam pojma kak da iš napravim \n")
diff = input("")
    
if int(diff) == 1:
    Fake_Chance = 100
    min = 0
    max = 5
elif int(diff) == 2:
    Fake_Chance = 20
    min = 6
    max = 9
elif int(diff) == 3:
    Fake_Chance = 10
    min = 10
    max = 15
elif int(diff) == 4:
    Fake_Chance = 7
    min = 16
    max = 20
elif int(diff) == 5:
    min = int(input("min = "))
    max = int(input("max = "))
    Fake_Chance = int(input("max = "))

elif int(diff) == 0:
    print("Ok slušaj vamo. Žnači nakon što odabereš težinu (Veličina riječi i kompleksitet ovise o težini)\npojavit će ti se neka nasumična riječ iz koje su Č i Ć zamjenjeni s C\n i onda ti trebaš prepisat CJELU riječ i zamijenit C sa Č ili Ć. \n!!!U nekim riječima može biti više praznih C-ova. \nnpr. Dva prazna C-a jedan može biti Č a drugi Ć, a također može biti da je jedan Č a drugi ostaje prazan\nE da nije mi se dalo isprogramirat da te vrati na početak pa sam zatvori i otvori ponovo :)")
    x = input()

for i in range(0,100):

    upit = meko()

    #while len(upit)-1 < min or len(upit)-1 > max: Stari code koji sam svrstava diffuculty po velicini rijeci
    #    upit = meko()

    clean = cleaning(upit)

    print("\nZadatak {}: {}".format(i+1,clean))

    user = str(input("Odgovor {}: ".format(i+1)))

    user = user.strip()
    upit = upit.strip()


    if str(user) == str(upit):
        tocno = tocno + 1
        print("Bravo tocno!")
        print("Statistika: {}/{} Postotak: {:.2f}%".format(tocno,tocno+netocno,(tocno/(tocno+netocno))*100))
    else:
        netocno = netocno + 1
        print("Hahaa glupan tocan odgovor je: {}".format(upit))
        print("Statistika: {}/{} Postotak: {:.2f}%".format(tocno,tocno+netocno,(tocno/(tocno+netocno))*100))

x = input("")
