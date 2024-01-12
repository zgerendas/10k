def hasonlit(szam1,szam2):
    if szam1 > szam2:
        print(szam1,"a nagyobb")
    elif szam1 < szam2:
        print(szam2,"a nagyobb")
    else:
        print("Egyenlők")
hasonlit(1,2)
hasonlit(10,3)
hasonlit(5,5)

def osszeg( lista):
    ossz=0
    for szam in lista:
        ossz += szam
    return ossz

#osszeg("alma")
print(osszeg([1,2,3,4]))

l = [2,3,5,7,8]
o = osszeg(l)
print(l,"lista eleminek összege:",o)
print(f"{l} lista eleminek összege: {o}")
