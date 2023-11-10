import random
random.seed(1)
gondolt = random.randint(1,100)
ismeteld = True
tippSzam = 0
while ismeteld:
    egesz = 0
    while egesz < 1 or egesz > 100:
        egesz = int(input("Kérek egy számot 1 és 100 között: "))
    tippSzam += 1
    if gondolt < egesz:
        print("Nagy")
    elif gondolt > egesz:
        print("Kicsi")
    else:
        print(tippSzam,"Lépesben talált!!")
        ismeteld = False
        #break



