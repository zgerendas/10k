'''
egy = 1
print(egy)
print(type(egy))

#egy=2      nem szerencsés
#print(egy)

szám = 12               # nagyon nem szerencsés!!! az á!!
print(type(szám),szám)

szam = 13       
print(type(szam),szam)

Szam = 14
print(type(Szam),Szam)
print('-'*10)

szam = szam + egy
print(type(szam),szam)

szam += egy
print(type(szam),szam)
szam += 10
print(szam)

szam -= 10
print(szam)

szam *= 10
print(szam)

szam /= 10
print(type(szam),szam)

szam = 17
szam //= 3              # egész osztás
print(type(szam),szam)

szam = 17
szam %= 3               # osztási maradék
print(type(szam),szam)

szam ="Alma "*5         # nem szerencsés típus és név
print(type(szam),szam)

'''
tp = 1,3
print(type(tp),tp)

tp = (1,3,'a',3)
print(type(tp),tp)

x = [1,3,'a',3]
print(type(x),x)

x = {1,3,'a',3}
print(type(x),x)


x,y = 12,'pipacs'

print(x)
print(y)

# x,y,z = 1,2
#x,y,z = 1,2,3,4
x,y,z = 1,2,3

# x + y = 12

