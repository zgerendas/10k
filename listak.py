import random

'''
lista = list()
szam = 1
while szam !=0 :
    #szam = int(input("Kérek egy egész számot: "))
    valasz = input("Kérek egy egész számot: ")
#    if valasz.isnumeric():
    if valasz.isdigit():
        szam = int(valasz)
        lista.append(szam)
print(lista)

lista = list()

for i in range(100):
    veletlen = random.randint(1,100)
    if lista.count(veletlen) == 0:
        lista.append(veletlen)
print(lista)

lista.sort()
print(lista)

lista.clear()
while len(lista) < 100:
    veletlen = random.randint(1,100)
    if lista.count(veletlen) == 0:
        lista.append(veletlen)
print(lista)

lista.sort()
print(lista)
print('-'*10)
lista.clear()

lista = list()
while len(lista) < 5:
    veletlen = random.randint(1,90)
    if lista.count(veletlen) == 0:
        lista.append(veletlen)
print(lista)

lista.sort()
print(lista)

lista2 = ["alma","körte","barack"]

#lista.append(lista2)
#lista.append(lista2.copy())
lista.extend(lista2)
print(lista)

lista2.append("banán")
print(lista,lista2,sep="\n")

print(lista.index('alma'))

lista.extend(lista)
print(lista)

print(lista.index('alma',6))

lista.reverse()
print(lista)

print(lista.__add__(lista2))

lista = [1,2,3,5]
lista.insert(3,4)
print(lista)
'''

halmaz = set()
#print(type(halmaz))
halmaz.add(1)
halmaz.add(3)
halmaz.add(2)
print(halmaz)

halmaz2 = {3,4,5}
print(halmaz.difference(halmaz2))
print(halmaz.intersection(halmaz2))
print(halmaz.symmetric_difference(halmaz2))
print(halmaz.union(halmaz2))