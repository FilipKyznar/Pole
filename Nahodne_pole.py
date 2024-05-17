import random

pole1 = []
pole2 = []

for x in range(random.randint(1,10)):
    pole1.append(random.randint(1,10))

print(pole1)

for x in range(random.randint(1,10)):
    pole2.append(random.randint(1,10))

print(pole2)

if len(pole1) > len(pole2):
    print("mensi pole je vetsi")
elif len(pole1) < len(pole2):
    print("vetsi pole je mensi")
else: print ("jsou stejne")   