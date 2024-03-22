#1
'''
szamok = list()
while True:
    be = input("Kérek egy számot: ")
    if be == "":
        break
    else:
        szamok.append(float(be))

szamok = list()
ismetled = True
while ismetled:
    be = input("Kérek egy számot: ")
    if be == "":
        ismetled = False
    else:
        szamok.append(float(be))

szamok = list()
be = "1"
while be != "":
    be = input("Kérek egy számot: ")
    if not be == "":
        szamok.append(float(be))
print(szamok)
print("------------- 1. feladat -------------")
print(f"A listában {min(szamok)} a legkisebb.")
print(f"A listában {max(szamok)} a legnagyobb.")

mini = szamok[0]
for szam in szamok:
    if szam < mini:
        mini = szam

maxi = szamok[0]
for szam in szamok:
    if szam > maxi:
        maxi = szam

print(f"A listában {mini} a legkisebb.")
print(f"A listában {maxi} a legnagyobb.")

'''

#2.a
def harommal_oszthatok(lista):
    db = 0
    for szam in lista:
        if szam % 3 == 0:
            db += 1
    return db
#print(harommal_oszthatok([1,2,3,4,5,6]))

#2.b
import random
szamok = list()
for _ in range(20):
    szamok.append(random.randint(1,100))

szamok = [random.randint(1,100) for _ in range(20)]
#2.c
print('------------- 2.c feladat -------------')
print(f'A listában {harommal_oszthatok(szamok)} darab hárommal osztható szám szerepelt.')

l = [23,4,5,6,88,99]

db = sum(1 for s in l if s % 3 ==0 )
print(db)

