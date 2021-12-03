thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
x = thisdict["model"]
print(x)
thisdict["year"] = 2020
print(thisdict)

for x in thisdict:
    print(x)  # prints the indexes like brand, model, year
for x in thisdict:
    print(thisdict[x])  # prints the index values like Ford, Mustang, 2020

for x in thisdict.values():
    print(x)  # prints the index values like Ford, Mustang, 2020

for x, y in thisdict.items():
    print(x, y)  # prints the index values along with the indexes

if "model" in thisdict:
    print('Yes, "model" is one of the keys in the "thisdict" dictionary')

print(len(thisdict))  # length of the dictionary

thisdict["color"] = "red"  # adds a new index
print(thisdict)

thisdict.pop("model")  # removes a particular index
print(thisdict)

thisdict.popitem()
print(thisdict)  # removes the last index

vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
print(vowels)

vowels2 = dict([(1, 'a'), (2, 'e'), (3, 'i'), (4, 'o'), (5, 'u')])
print(vowels2)

print(vowels[1])
print(vowels.keys())
print(vowels.values())

