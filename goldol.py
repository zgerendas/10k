import random
'''
for i in range(10):
    print(random.random())

for i in range(1000):
    print(random.randint(1,100),end=',')
'''
gondolt = random.randint(1,100)
ismetled = True

while ismetled:
    egesz = int(input("Kérek egy számot 1 és 100 között: "))
    if egesz < 1 or egesz > 100:
        print("Hibás szám")
    else:
        ismetled = False