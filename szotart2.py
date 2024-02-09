mondat = "Ut consequat cupidatat adipisicing id minim aliquip voluptate do. Non aute aliquip laborum ut in Lorem aute anim enim nulla esse cupidatat."

#print(mondat.lower())
#mondat = mondat.lower()
#mondat = mondat.replace(".","")
mondat = mondat.replace(".","").lower().replace(" ","")

print(mondat)
betuk = dict()

'''
for kar in mondat:
    if betuk.get(kar) == None:
        betuk.update({kar:1})
    else:
        betuk.update({kar:betuk.get(kar)+1})
print(betuk)

betuk.clear()
for kar in mondat:
    db = betuk.get(kar)
    if db == None:
        betuk.update({kar:1})
    else:
        betuk.update({kar:db + 1})
print(betuk)
'''
betuk.clear()
for kar in mondat:
    db = betuk.get(kar)
    if not (kar in betuk):
        betuk.update({kar:1})
    else:
        betuk.update({kar:db + 1})
print(betuk)

#print(betuk.pop('ubul'))
#print(betuk)

#print(betuk.popitem())
#print(betuk)

max = 0
kar = ""
for k,e in betuk.items():
    if e > max:
        max = e
        kar = k
print(kar,max)

bet = input("Kérek egy betűt: ")
if bet in betuk.keys():
    print(bet+" betű "+str(betuk[bet]) +" alkalommal szerpelt a mondatban.")
    print(f"{bet} betű {betuk[bet]} alkalommal szerpelt a mondatban.")
else:
    print(bet+" betű nem szerpelt a mondatban.")

valid = "qwertzuiopasdfghjklyxcvbnm"
'''
while True:
    kar = input("Kérek az angol ABC-ből egy betűt: ")
    if kar  in valid:
        break

ismeteld = True
while ismeteld:
    kar = input("Kérek az angol ABC-ből egy betűt: ")
    if kar  in valid:
        ismeteld = False
'''
kar = " "
while not (kar in valid):
    kar = input("Kérek az angol ABC-ből egy betűt: ").lower()

#print("" in valid)
print(sorted(valid))
valid = sorted(valid)
kar = " "
while not (kar in valid):
    kar = input("Kérek az angol ABC-ből egy betűt: ").lower()
    if not (kar in valid):
        print("Nem az angol ABC betűjét írtad!")
print(kar*10)

print(str(valid))

szoveg =""
for elem in valid:
    szoveg += elem
print(szoveg)