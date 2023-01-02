# kerulet : 0 | szavazok : 1 | vezetek_nev : 2 | keresztnev : 3 | tamogatja : 4
osszes_szavazat = 0
max_szavazat = 12345
f = open("szavazatok.txt", "r", encoding='UTF-8')

adatok : list[list[str]] = []

for i in f:
    sor = i.strip()
    sor = sor.split(" ")
    adatok.append(sor)

for i in range(len(adatok)):
    adatok[i][4] = adatok[i][4].replace("-","független")

def Feladat2(): 
    print(f"A helyhatósági választáson {len(adatok)} képviselőjelölt indult.")

def Feladat3():
    vezetek_nev = input("Vezeték Név: ")
    kereszt_nev = input("Kereszt Név: ")

    teljes_nev = (vezetek_nev + " " + kereszt_nev)

    for i in range(len(adatok)):
        if teljes_nev == (adatok[i][2] + " " + adatok[i][3]):
            print(teljes_nev + f" összesen {adatok[i][1]} szavazatot kapott")
            break
    else:
        print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")

def Feladat4():
    global osszes_szavazat
    for i in range(len(adatok)):
        osszes_szavazat = osszes_szavazat + int(adatok[i][1])
    
    szazalek = ((osszes_szavazat/float(max_szavazat))*100).__round__(2)
    print(f"A választáson {osszes_szavazat} állampolgár, a jogosultak {szazalek}%-a vett részt.")

def szamitas(szam):
    szazalek = ((szam/float(osszes_szavazat))*100).__round__(2)
    return szazalek

def Feladat5():
    gyep = 0
    hep = 0
    tisz = 0 
    zep = 0
    fuggetlen = 0

    for i in range(len(adatok)):
        if adatok[i][4] == "ZEP":
            zep += int(adatok[i][1])
        if adatok[i][4] == "GYEP":
            gyep += int(adatok[i][1])
        if adatok[i][4] == "HEP":
            hep += int(adatok[i][1])
        if adatok[i][4] == "TISZ":
            tisz += int(adatok[i][1])
        if adatok[i][4] == "független":
            fuggetlen += int(adatok[i][1])
    
    print(f"\nZöldségevők Pártja= {szamitas(zep)}%\n",
          f"Gyümölcsevők Pártja= {szamitas(gyep)}%\n",
          f"Húsevők Pártja= {szamitas(hep)}%\n",
          f"Tejivók Pártja= {szamitas(tisz)}%\n",
          f"Függetlenek= {szamitas(fuggetlen)}%\n",
                )


def Feladat6():
    partok = ["GYEP", "ZEP", "TISZ", "HEP"]
    legnagyobb = 0
    for i in range(len(adatok)):
        if int(adatok[i][1]) > legnagyobb:
            legnagyobb = int(adatok[i][1])
    
    for i in range(len(adatok)):
        if int(adatok[i][1]) == legnagyobb:
            if partok.__contains__(adatok[i][4]):
                print(f"{adatok[i][2]} {adatok[i][3]} érte el a legtöbb szavazatot. Támogatja: {adatok[i][4]}")
            else:
                print(f"{adatok[i][2]} {adatok[i][3]} érte el a letöbb szavazatot. Független.")



def Feladat7():
    korzetek : list = []
    for i in range(len(adatok)):
        if korzetek.count(adatok[i][0]) == 0:
            korzetek.append(adatok[i][0])

    konyvtar : dict = {}
    korzetek.sort()

    for i in range(len(korzetek)):
        konyvtar[i] = ['0', '0', '0', '0','0']

    for i in range(len(adatok)):
        for k in range(len(korzetek)):
            if int(korzetek[k]) == int(adatok[i][0]):
                if int(adatok[i][1]) > int(konyvtar.get(k)[1]):
                    konyvtar.__setitem__(k, adatok[i])
    w = open("kepviselok.txt", "w", encoding='UTF-8')
    
    for i in konyvtar:
        w.write(f"{konyvtar[i][0]} {konyvtar[i][1]} {konyvtar[i][2]} {konyvtar[i][3]} {konyvtar[i][4]} | ")
    w.close()

Feladat2()  
Feladat3()
Feladat4()
Feladat5()
Feladat6()
Feladat7()