'''
print("Kérem a neved: ",end="")
nev = input()
print("Szia "+nev)

nev = input("Kérem a neved 2: ")
print("Szia "+nev)

szam = input("Kérek egy számot 1 és 10 között: ")
print(szam)
print(szam*2)
print(type(szam))   # szöveget ad vissza az input !!!

szam = int(input("Kérek egy számot 1 és 10 között: "))
print(szam)
print(szam*2)
print(type(szam))

szam = float(input("Kérek egy számot 1 és 10 között: "))
print(szam)
print(szam*2)
print(type(szam))

szam = input("Kérek egy egész számot 1 és 10 között: ")
egesz = int(szam)
print(egesz*2)

beolvasott = input("Kérek valamit: ")
print(beolvasott)
print(type(beolvasott))
print(list(beolvasott))
print(set(beolvasott))
print(tuple(beolvasott))

szam = input("Kérek egy egész számot 1 és 10 között: ")
egesz = int(szam)

if egesz < 1:
    print("A szám túl kicsi!")
else:
    if egesz > 10:
        print("A szám túl nagy!")
print("-"*10)

if egesz < 1:
    print("A szám túl kicsi!")
elif egesz > 10:
    print("A szám túl nagy!")

print(13 % 2, 13 // 2)

egesz = int(input("Kérek egy egész számot: "))
maradek = egesz % 2
if maradek == 0:
    print("Páros")
else:
    print("Páratlan")

egesz = int(input("Kérek egy egész számot: "))
#maradek = egesz % 2
if egesz % 2 == 0:
    print("Páros")
else:
    print("Páratlan")


egesz = int(input("Kérek egy egész számot: "))
pozitiv = egesz > 0
#print(type(pozitiv),pozitiv)
if pozitiv:
    print("pozitív")
if egesz < 0:
    print("Negatív")
if egesz == 0:
    print("Nulla")

print("-"*10)

if egesz == 0:
    print("Nulla")
elif egesz > 0:
    print("Pozitív")
else:
    print("Negatív")
'''

egesz = int(input("Kérek egy egész számot: "))
if egesz % 3 == 0:
    print("Osztható")
else:
    print("Nem osztható")

