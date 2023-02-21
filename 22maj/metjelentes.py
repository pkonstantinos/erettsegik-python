#1. feladat
telepules = []
ido = []
szelirany = []
homerseklet = []

with open("tavirathu13.txt", "r", encoding="UTF-8") as f:
    for i in f:
        sor = i.strip().split(" ")
        telepules.append(sor[0])
        ido.append([sor[1][0:2], sor[1][2:4]])
        szelirany.append([sor[2][0:3], sor[2][3:5]])
        homerseklet.append(int(sor[3]))




def Feladat2():
    print("2. feladat")
    bekeres = input("Adja meg egy település kódját! Település: ")
    indexe = 0
    for i, v in enumerate(telepules):
        if v == bekeres:
            indexe = i
    print(f"Az utolsó mérési adat a megadott településről {ido[indexe][0]}:{ido[indexe][1]}-kor érkezett")




def Feladat3():
    print("3. feladat")
    legalacsonyabb = 0
    legmagasabb = 0
    for i, v in enumerate(homerseklet):
        if v < homerseklet[legalacsonyabb]:
            legalacsonyabb = i
        if v> homerseklet[legmagasabb]:
            legmagasabb = i
    print(f"A legalacsonyabb hőmérséklet: {telepules[legalacsonyabb]} {ido[legalacsonyabb][0]}:{ido[legalacsonyabb][1]} {homerseklet[legalacsonyabb]} fok.")
    print(f"A legmagasabb hőmérséklet: {telepules[legmagasabb]} {ido[legmagasabb][0]}:{ido[legmagasabb][1]} {homerseklet[legmagasabb]} fok.")




def Feladat4():
    print("4. feladat")
    for i, v in enumerate(szelirany): 
        if v[0:2] == ['000', '00']:
            print(f"{telepules[i]} {ido[i][0]}:{ido[i][1]}")


def Feladat5():
    print("5. feladat")
    telepulesek_neve = []
    for v in telepules:
        if not v in telepulesek_neve:
            telepulesek_neve.append(v)
    telep_dict = {}
    telep_inga = {}
    for i in telepulesek_neve:
        telep_dict[i] = [None, None, None, None]
        telep_inga[i] = []
    
    for i in range(len(telepules)):
        for v in telepulesek_neve:
            if telepules[i] == v:
                
                if int(ido[i][0]) == 1:
                    if telep_dict[v][0] is None:
                        telep_dict[v][0] = homerseklet[i]
                if int(ido[i][0]) == 7:
                    if telep_dict[v][1] is None:
                        telep_dict[v][1] = homerseklet[i]
                if int(ido[i][0]) == 13:
                    if telep_dict[v][2] is None:
                        telep_dict[v][2] = homerseklet[i]
                if int(ido[i][0]) == 19:
                    if telep_dict[v][3] is None:
                        telep_dict[v][3] = homerseklet[i]

                telep_inga.get(v).append(homerseklet[i])


    kozephomerseklet = []
    for i,v in telep_dict.items():
        if not None in v:
            ingadozas = max(telep_inga.get(i)) - min(telep_inga.get(i))
            atlag = round((v[0] + v[1] + v[2] + v[3]) / len(v))
            kozephomerseklet.append([i, atlag, ingadozas])
        else:
            ingadozas = max(telep_inga.get(i)) - min(telep_inga.get(i))
            kozephomerseklet.append([i, "NA", ingadozas])
    
    for i in kozephomerseklet:
        if i[1] == "NA":
            print(f"{i[0]} {i[1]}; Hőmérséklet-ingadozás: {i[2]}")

        else:
            print(f"{i[0]} Középhőmérséklet: {i[1]}; Hőmérséklet-ingadozás: {i[2]}")
    
        
def Feladat6():
    print("6. feladat")
    telepulesek_neve = []
    for v in telepules:
        if not v in telepulesek_neve:
            telepulesek_neve.append(v)
    

    feladat_6 = {}
    for i in telepulesek_neve:
        feladat_6[i] = []
    for i in range(len(telepules)):
        for v in telepulesek_neve:
            if telepules[i] == v:
                feladat_6.get(v).append([ido[i][0] +":" +ido[i][1], "#"*int(szelirany[i][1])])
    for i in telepulesek_neve:
        f = open(f"{i}.txt", "w")
        f.write(i +"\n")
        for v in feladat_6.get(i):
            f.write(f"{v[0]} {v[1]}\n")
        f.close()
    print("A fájlok elkészültek.")


    
 
Feladat2()
Feladat3()
Feladat4()
Feladat5()
Feladat6()