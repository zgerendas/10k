import random

def genList(darab,kezd=1,veg=100):
    lista = list()
    for i in range(darab):
        #v = random.randint(kezd,veg)
        #lista.append(v)
        lista.append(random.randint(kezd,veg))
    return lista
'''
print(genList(10,10,20))
print(genList(10,-10,20))
print(genList(0,0,0))
print(genList(10,5))
'''
listam = genList(100)

# megszamolás

def megszamol(l):
    db = 0
    for elem in l:
        if elem > 50:
            db += 1     # db++; db = db +1
    return db

print(megszamol(listam))

# eldontés
def eldont(l):
    van = False
    for elem in l:
        #print(elem,end=", ")
        if elem > 50:
            van = True
    #print()
    return  van  

print(listam)

print(eldont(listam))

# eldontés 2
def eldont2(l):
    van = False
    for elem in l:
        print(elem,end=", ")
        if elem > 50:
            van = True
            break
    print()
    return  van  
print(eldont2(listam))

# eldontés 3
def eldont3(l):
    i = 0
    while not (l[i] > 50) and i < len(l)-1:
        print(l[i])
        i += 1
    return l[i] > 50
print(eldont3(listam))

# kivalogatás
def kivalogatas(l):
    lst = list()
    for elem in l:
        if elem > 50:
            lst.append(elem)
    return lst
print(kivalogatas(listam))
    
# kiválasztás
def kivalasztas(l):
    talat = None
    for elem in l:
        print(elem,end=", ")
        if elem > 50:
            talat = elem
            break
    print()
    return  talat
print(kivalasztas(listam))

# összegzes
def osszegezes(l):
    ossz = 0
    for elem in l:
            ossz += elem
    return ossz

print(osszegezes(listam))
print(sum(listam))