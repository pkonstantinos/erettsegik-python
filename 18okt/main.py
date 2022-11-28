
#Feladat1
import random
import string

paros = []
hosszusag = []
kerites = []
hazszam = []


f = open("kerites.txt", "r", encoding='utf-8')

for sor in f:
    ujsor = sor.strip()
    splittelve = ujsor.split(" ")

    paros.append(splittelve[0])
    hosszusag.append(splittelve[1])
    kerites.append(splittelve[2])
f.close()

def Feladat2():
    osszes = 0
    for i in hosszusag:
        osszes += 1

    print(f"2. feladat\nAz eladott telkek száma: {osszes}\n")

def Feladat3():
    parosok = 0
    paratlanok = 1
    for i in range(paros.__len__()):
        if paros[i] == "0":
            parosok = parosok + 2
            hazszam.append(parosok)
        else:
            if i > 1:
                paratlanok = paratlanok + 2
                hazszam.append(paratlanok)
            else:
                hazszam.append(paratlanok)




    if paros[hazszam.__len__()-1] == "0":
        print(f"3. feladat\nA páros oldalon adták el az utolsó telket.\nAz utolso telek házszáma: {parosok}\n")
    else:
        print(f"3. feladat\nA páratlan oldalon adták el az utolsó telket.\nAz utolso telek házszáma: {paratlanok}\n")





def Feladat4():

    for i in range(paros.__len__()):
        if i > 1:
            if paros[i] == "1":
                if kerites[i - 1] == kerites[i] or kerites[i + 1] == kerites[i]:
                    print(f"4. feladat\nA szomszéddal egyezik a kerítés színe: {hazszam[i]}")



def Feladat5():
    bekeres = int(input("Adjon meg egy házszámot! "))
    print(f"A kerítés színe / állapota: " + str(kerites[hazszam.index(bekeres)]))
    elotteSzomszed = kerites[hazszam.index(bekeres)-1]
    utanaSzomszed = kerites[hazszam.index(bekeres)+1]
    azLetters = []
    for letter in string.ascii_uppercase:
        azLetters.append(str(letter))

    newAzLetters = []
    for i in azLetters:
        if i != str(kerites[hazszam.index(bekeres)]) and i != str(elotteSzomszed) and i != str(utanaSzomszed) :
            newAzLetters.append(str(i))
    print(f"Egy lehetséges festési szín: {random.choice(newAzLetters)}")


def Feladat6():
    f = open("utcakep.txt", "w", encoding="utf-8")
    for i in range(kerites.__len__()):
        if paros[i] == "1":
            f.write(kerites[i]*int(hosszusag[i]))

    f.write("\n")
    for i in range(kerites.__len__()):
        if paros[i] == "1":
            f.write(str(hazszam[i]) + (" "*(int(hosszusag[i]) - str(hazszam[i]).__len__())))
    f.close()



Feladat2()
Feladat3()
Feladat4()
Feladat5()
Feladat6()



