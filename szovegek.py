mondat = "Est magna ullamco aliquip dolore laborum duis."

db = 0
for c in mondat:
    if c == " ":
        db += 1
print(db+1)

print(mondat.count(" ")+1)

lista = mondat.split(" ")
print(len(lista))

mondat = "Consequat    magna adipisicing    aute dolore cupidatat officia."
print(mondat.count(" ")+1)
lista = mondat.split(" ")
print(len(lista))
print(lista)

print(mondat)
#print(mondat.replace("  "," "))

'''
while len(mondat) >  len(mondat.replace("  "," ")):
    mondat = mondat.replace("  "," ")
    print(mondat)
print(mondat.count(" ")+1)
'''
while "  " in mondat:
    mondat = mondat.replace("  "," ")
    print(mondat)
print(mondat.count(" ")+1)


mondat = " Consequat    magna adipisicing    aute dolore cupidatat officia. "
mondat2 = mondat
while "  " in mondat:
    mondat = mondat.replace("  "," ")
   # print(mondat)
print(mondat.count(" ")+1)
db = mondat.count(" ")+1
if mondat.startswith(" "):
    db -= 1
if mondat.endswith(" "):
    db -= 1
print(db)
'''
lista = mondat2.split(" ")
print(lista)

#print(lista.remove(''))
lista.remove('')
print(lista)

while '' in lista:
    lista.remove('')
#print(lista)
print(len(lista))
'''

lista = mondat2.split(" ")
while '' in lista:
    lista.remove('')
print(len(lista))

lista = mondat2.split(" ")

#print(lista.pop(0))
#print(lista.pop(1))
#print(lista)
"""
for i  in range(len(lista)):
    #print(i,lista[i])
    if lista[i] == '':
        lista.pop(i)    # !!!!!!!!!!!! NE
"""

lista2 = lista.copy()
#lista2 = lista
for i  in range(len(lista)-1,-1,-1):
    #print(i,end=" ")
    if lista[i] == '':
        lista2.pop(i) 

print(lista2)
print(lista)



