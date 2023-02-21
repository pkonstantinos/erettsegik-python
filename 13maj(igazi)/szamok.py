import random

temakor = []
pontok = []
helyes_valasz = []
kerdes = []


f = open("felszam.txt","r", encoding="UTF-8")
files = f.readlines()
for i in range(1,len(files),2):
    elso = files[i-1].strip()
    masodik = files[i].strip().split()
    kerdes.append(elso)
    temakor.append(masodik[2])
    pontok.append(int(masodik[1]))
    helyes_valasz.append(int(masodik[0]))


print("2. feladat")
print(f"Összesen {len(kerdes)} feladat található")

print("3. feladat")
harom = 0
ketto = 0
egy = 0
for i, v in enumerate(pontok):
    if temakor[i] == "matematika":
        if pontok[i] == 3:
            harom +=1
        elif pontok[i] ==2:
            ketto +=1
        else:
            egy +=1
matek = temakor.count("matematika")
print(f"Az adatfajlban {matek} matematika feladat van, 1 pontot er\n {egy} feladat, 2 pontot er {ketto} feladat, 3 pontot er {harom} feladat. ")

print("4. feladat")
print(f"{min(helyes_valasz)} -tól {max(helyes_valasz)} -ig terjednek a számértékek")


print("5. feladat")

temakor_dict = {}
for i in temakor:
    temakor_dict[i] = []
print("Ilyen témakörök találhatóak a feladatsorban: ")
for i, v in temakor_dict.items():
    print(i)

print("6. feladat")

for i in range(len(temakor)):
    temakor_dict.get(temakor[i]).append([i, kerdes[i], pontok[i], helyes_valasz[i]])


temakor_neve = input("Milyen temakorbol szeretne kerdest kapni? ")
random_feladat = random.choice(temakor_dict.get(temakor_neve))
valasz = int(input(f"{random_feladat[1]} "))
elert_pont = 0
if valasz == random_feladat[3]:
    elert_pont += random_feladat[2]

if elert_pont == 0:
    print("A valasz 0 pontot ert")
    print(f"A helyes valasz: {random_feladat[3]}")
else:
    print(f"A valasz {elert_pont} pontot ert")


print("7. feladat")

random_Temakorok_7 = []
for i in range(10):
    random_temakor = random.choice(list(temakor_dict))
    random_kerdes = random.choice(temakor_dict.get(random_temakor))
    while random_kerdes in random_Temakorok_7:
        random_kerdes = 0
        random_kerdes = random.choice(temakor_dict.get(random_temakor))
    random_Temakorok_7.append(random_kerdes)

cf = open("tesztfel.txt", "w")
ossz_pontszam = 0
for v in random_Temakorok_7:
    ossz_pontszam += v[2]

for v in random_Temakorok_7:
    kiiras = f"{v[2]} {v[1]}\n"
    cf.write(kiiras)
kiiras_2 = f"A feladatsorra osszesen {ossz_pontszam} pont adhato."
cf.write(kiiras_2)

