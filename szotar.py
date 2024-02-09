'''
v = ()
print(type(v))

v = []
print(type(v))

v = {}
print(type(v))

v = tuple()
print(type(v))

v = list()
print(type(v))
v.append(1)
v.append(2)
v.append(1)
print(v)

v= set()
print(type(v))
v.add(1)
v.add(2)
v.add(1)
print(v)

v= dict()
print(type(v))

szotar = {"név":"Pista","kor":14}
print(szotar)
print(szotar["név"])

szotar.update({"nem":"fiú"})
print(szotar)

szotar.update({"név":"Zalán"})
print(szotar)

szotar["név"]="Károly"
print(szotar)
szotar["szdate"]="1999.9.9"
print(szotar)

szoveg = "Adipisicing consectetur commodo ut proident irure. Pariatur officia labore exercitation laboris consectetur Lorem adipisicing voluptate excepteur Lorem."

#print(szoveg.replace(".","").split(" "))
lista = szoveg.replace(".","").split(" ")
szotar =dict()
szotar.clear()
db = 1
for szo in lista:
    szotar[db] = szo
    #szotar.update({db,szo})
    db += 1
print(szotar)

print(szotar[2])
print(len(szotar))

for x in szotar:
    print(x,end=", ")
print()

for x in szotar:
    print(szotar[x],end=", ")
print()

#print(szotar.keys())
#v  = szotar.keys()
#print(type(v))
for x in szotar.keys():
    print(x,end=", ")
print()


for x in szotar.values():
    print(x,end=", ")
print()

for kulcs,ertek in szotar.items():
    print(kulcs,ertek,sep=":",end=", ")
print()

'''
szemelyek = list()
szemely = {"név":"Pista","kor":14}
szemelyek.append(szemely)

szemely = {"név":"Ágnes","kor":15}
szemelyek.append(szemely)

szemely = {"név":"Laci","kor":14}
szemelyek.append(szemely)

szemely = {"név":"Éva","kor":13}
szemelyek.append(szemely)

print(szemelyek)

for sz in szemelyek:
    print(sz["név"])

kor =14 # int(input("Kérem az életkort: "))
for sz in szemelyek:
    if sz["kor"] == kor:
        print(sz["név"])

osszeg = 0
db = 0
for sz in szemelyek:
    osszeg += sz["kor"]
    db +=1
#print(osszeg/db)
print(osszeg/len(szemelyek))
   

for sz in szemelyek:
    sz["kor"] +=1

print(szemelyek)
