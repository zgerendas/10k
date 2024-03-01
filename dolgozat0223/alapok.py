'''
#1
knev = input("Kérem a keresztneved: ")
vnev = input("Kérem a vezeték neved: ")
teljes_nev = vnev+" "+knev
print("Üdvözöllek",teljes_nev)
print(f"Üdvözöllek {teljes_nev}")

#2
import random
szamok = list()
for i in range(10):
    szamok.append(random.randint(1,10))

szamok = [random.randint(1,10)  for i in range(10)]
#print(szamok)
beSzam = int(input("Kérek egy egész számot 1 és 7 között: "))
if beSzam in szamok:
    print("A szám a listában volt.")
else:
    print("A szám nincs a listában.")

print("A lista: ",end="")
for szam in szamok:
    print(szam,end=", ")
print()
#3
fajl = open("szamok.txt","w")
for szam in szamok:
    fajl.write(str(szam)+"\n")
fajl.close()

#4
def addSzor(a,b):
    return (a+b)*2

print(f"Eredmény: 2,3 -> {addSzor(2,3)}")
'''
versenyzok = list()
f = open("snooker.txt")
fejLec = f.readline()
for sor in f:
    sorLista = sor.replace("\n","").split(";")
    szotar = {
        "Helyezes":int(sorLista[0]),
        "Nev":sorLista[1],
        "Orszag":sorLista[2],
        "Nyeremeny":int(sorLista[3])
    }
    #print(szotar)
    versenyzok.append(szotar)
f.close()

#print(versenyzok)
print(f"5.2. feladat: A világranglistán {len(versenyzok)} versenyző szerepel")

osszeg = 0
for versenyzo in versenyzok:
    osszeg += versenyzo["Nyeremeny"]

#print(osszeg/len(versenyzok))
print(f"5.3. feladat: A versenyzők átlagosan {osszeg/len(versenyzok)} fontot kerestek")

db = 0
for versenyzo in versenyzok:
    if  versenyzo["Orszag"] == "Anglia":
        db += 1
print(f"5.4. feladta: {db}-en indultak Angliábol")

for versenyzo in versenyzok:
    if  versenyzo["Helyezes"] == 1:
        break
print(versenyzo)

ismeteld = True
index = 0
while ismeteld:
    if versenyzok[index]["Helyezes"] == 1:
        ismeteld = False
        print(versenyzok[index])
    index +=1

ismeteld = True
index = 0
while ismeteld:
    v =versenyzok[index]
    if v["Helyezes"] == 1:
        ismeteld = False
    index +=1
print(v)

index = 0
while versenyzok[index]["Helyezes"] != 1:
    index +=1

print(versenyzok[index])


max = 0

