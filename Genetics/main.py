import random

A1 = "00000000"
A2 = "11111111"
A3 = "10101010"
A4 = "01010101"

List = [A1, A2, A3, A4]
newList = []
List1 = []
for x in List:
    y = - int(x) * int(x) + 5
    newList.append(y)

print(List)
print("Fittest one:", newList[0])
List.sort()
print(List)

FirstFit = List[0]
SecondFit = List[1]

print(FirstFit[0:5] + SecondFit[5:8])
print(FirstFit[5:8] + SecondFit[0:5])

#ran = str((random.randint(0, 1)) + str((random.randint(0, 1)) + str((random.randint(0, 1))
#print(ran)
