#mondat = input("Kérek egy mondatot: ")
mondat ='Ez egy teszt mondat!'
print(len(mondat))

db = 0
for c in mondat:
    #print(c)
    if c == 'e' or c =='E':
        db +=1
print(db)

db = 0
for c in mondat.lower():
    if c == 'e':
        db +=1
print(db)

magan =('a','á','e','é','i','í','o','ó','ö','Ő','u','ú','ü','ű')

#print(mondat.find('teszt'))
#print(mondat.index('x'))
#print(magan.index('m'))
print(mondat)
db = 0
maganDB = set()
#print(type(maganDB))
for c in mondat.lower():
    for m in magan:
        if c == m:
            db +=1
            maganDB.add(c)
print(db)
print(len(maganDB),"különböző magánhangzó volt.")

print('*' + '  alma    '.strip() + '*')
print('*' + '  alma    '.rstrip() + '*')
print('*' + '  alma    '.lstrip() + '*')


print(mondat.split(' '))
print('1,2,3,4,5,6'.split(','))
print('1, 2, 3, 4, 5, 6'.split(','))
print('1, 2, 3, 4, 5, 6'.split(', '))



