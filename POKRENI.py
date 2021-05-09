
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

sys.setrecursionlimit(15000)



def cleaning():

    clean = re.sub('č', 'c', upit)
    clean = re.sub('ć', 'c', clean)

    clean = re.sub('Č', 'C', clean)
    clean = re.sub('Ć', 'C', clean)

    return clean


def mt():
    
    ran = random.randint(1,2)

    if ran == 1:
        upit = tvrdo()
    elif ran == 2:
        upit = meko()

    return upit


def meko():

    filepath = 'src/Sve_ć.txt'


    ran = random.randint(1,26491)
    
    fp = open(filepath, "r", encoding="UTF-8")
    for i, line in enumerate(fp):
        if i == ran:
            #print("meko Ran = {} RIjec = {}".format(ran,line))
            upit = line
            return upit
            break


    fp.close()   


def tvrdo():

    filepath = 'src/Sve_č.txt'


    ran = random.randint(1,73284)
    
    fp = open(filepath, "r", encoding="UTF-8")
    for i, line in enumerate(fp):
        if i == ran:
            #print("tvrdo 5Ran = {} RIjec = {}".format(ran,line))
            upit = line
            return upit
            break

    fp.close()   

print('Sve riječi izvučene su iz databaze Hrvatskog jezičnog portala.\nU toj databazi postoji 73284 riječi koje sadrže slovo Č i 26491 riječi koje sadrže slovo Ć\n\n Izvukao i programirao "Dr." "Prof." Vito Čuić\n E da i definitivno nisam i neću provijeriti jesu li točno napisane u databazi\n')


print("Odabir težine: \n 1) Lagano \n 2) Normalan lik \n 3) Teško \n 4) Profesor \n\n 0) POMOĆ nemam pojma kak da iš napravim \n")
diff = input("")
    
if int(diff) == 1:
    min = 0
    max = 5
elif int(diff) == 2:
    min = 6
    max = 9
elif int(diff) == 3:
    min = 10
    max = 15
elif int(diff) == 4:
    min = 16
    max = 20
elif int(diff) == 5:
    min = int(input("min = "))
    max = int(input("max = "))
elif int(diff) == 0:
    print("Ok slušaj vamo. Žnači nakon što odabereš težinu (Veličina riječi i kompleksitet ovise o težini)\npojavit će ti se neka nasumična riječ iz koje su Č i Ć zamjenjeni s C\n i onda ti trebaš prepisat CJELU riječ i zamijenit C sa Č ili Ć. \n!!!U nekim riječima može biti više praznih C-ova. \nnpr. Dva prazna C-a jedan može biti Č a drugi Ć, a također može biti da je jedan Č a drugi ostaje prazan\nE da nije mi se dalo isprogramirat da te vrati na početak pa sam zatvori i otvori ponovo :)")
    x = input()

for i in range(0,100):

    upit = mt()

    while len(upit)-1 < min or len(upit)-1 > max: 
        upit = mt()

    clean = cleaning()

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
