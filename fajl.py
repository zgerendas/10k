fajl = open("ub2017egyeni.txt")
#print(fajl.read())
#print(fajl.readline())
#print(fajl.readline())
#print(fajl.readlines())

versenyzok = list()
fejlec = fajl.readline()
for sor in fajl:
   # print(sor.replace('\n',"").split(";"))
    verenyzo = sor.replace('\n',"").split(";")
    #print(verenyzo[0])
    v = {"Versenyzo":verenyzo[0],"Rajtszam":verenyzo[1],"Kategoria":verenyzo[2],"Versenyido":verenyzo[3],"TavSzazalek":int(verenyzo[4])}
    versenyzok.append(v)
    #print(v)
fajl.close()

#print(versenyzok)

f = open("versenyzok.txt","w")

for v in versenyzok:
    #print(v["Versenyzo"])
    f.write(v["Versenyzo"])
    f.write("\n")
f.close()

ferfi = 0
for v in versenyzok:
    if v["Kategoria"] == "Ferfi":
        ferfi += 1
print("Férfi: ",ferfi)
print("Női: ",len(versenyzok)-ferfi)

db = 0
for v in versenyzok:
    if v["TavSzazalek"] == 100:
        db += 1
print(db,"100%-os")

minimum = 100
kicsi = ""
for v in versenyzok:
    if v["TavSzazalek"] < minimum:
        minimum = v["TavSzazalek"]
        kicsi = v["Versenyzo"]
print(minimum,kicsi)

osszeg = 0
for v in versenyzok:
    osszeg += v["TavSzazalek"]
print(osszeg / len(versenyzok))

