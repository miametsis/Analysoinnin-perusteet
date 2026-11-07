furniture = ["Sofa", "Bed" , "Mirror", "Table"]
print(furniture)

print(furniture[0])
print(furniture[1])

for item in furniture:
    if item == "Sofa" :
        print(item)


import random
thowDiceNumbers = [0, 0, 0,0 ,0]
for i in range(5):
throwDiceNumbers[i] = random.randint(1, 6)
print(throwDiceNumbers)
total = sum(throwDiceNumbers)
print("Sum is", total)
print("Highest number is:" , max(throwDiceNumbers))
