'''
szamok = [1,2,5,6,9]
for szam in szamok:
    print(szam)
    x = szam
    x += 10
print(x)

# elemek = {"alma",12,34,'k',[1,2]} - halmazban nem lehet lista
elemek = ("alma",12,34,'k',[1,2]) #  tuple
for x in elemek:
    print(type(x),x)

elemek = ["alma",12,34,'k',[1,2]] #  lista
for x in elemek:
    print(type(x),x)

#for (i = 1 ; i < 10; i++) {}

for i in range(1,11):
    #print(i,i*i)    # i**2 == i*i
    print(i,i*i,sep="^2 = ")


for i in range(2,101,2):
    #print(i,i*i)    # i**2 == i*i
    print(i,i*i*i,sep="^3 = ")

'''
'''
for i in range(10,-11,-3):
    print(i)

for x in ['a','b']:
        print(x)
for x in ['a','b']:
 print(x)
 print(x*2)


for x in ['a','b']:
#        print(x)
    None
for x in ['a','b']:
 print(x)
 print(x*2)
'''
lista=[1,23,44,5,8,12]
x=0
for e in lista:
    print(x,e)
    x +=1

print(len(lista))
print(lista[0],lista[5])
# print(lista[6])
print('-'*20)
for i in range(len(lista)):
    print(i,lista[i])


