# A set is an unordered collection with no duplicate values.

list = [1, 2, 3, 3, 4, 4]
set1 = set(list)
print(set1)

set2 = {5, 6, 7}
print(set2)

set3 = set1 | set2  # union
print(set3)

set4 = set1 & set2  # intersection
print(set4)

set5 = set1 - set2  # difference
print(set5)

vowels = ['a', 'e', 'i', 'o', 'u']
notvowel = {x for x in 'apple' if x not in vowels}
print(notvowel)
