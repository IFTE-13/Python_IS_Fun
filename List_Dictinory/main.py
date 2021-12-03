carname = input('Enter a car name: ')
cars = ["Ford", "Volvo", 'Bmw', carname]
a = len(cars)
print(a)

for x in cars:
    print(x)

cars.append('Ferrari')
cars.pop(0)
cars.remove('Volvo')
print(cars)

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

# Tuples are immutable, but can hold mutable objects.

tuple = ('a', 'b')
print(tuple)

s = 'a', 'b', [1, 2, 3]
print(s)

a = 'Hello, World!'
print(a)

# sub strings
print(a[1])
print(a[-1])
print(a[2:5])
print(a[-5:-2])
print(len(a))  # length

# multiple line
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)

print(a.strip())  # returns "Hello, World!"
print(a.lower())  # returns string as lower case
print(a.upper())  # returns string as upper case
print(a.replace("H", "J"))
print(a.split(" "))  # returns ['Hello', ' World!']

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# adding two strings
a = "Hello "
b = "World"
c = a + b
print(c)

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

thislist = ["apple", "banana", 4, "kiwi", "melon", "mango"]  # we can take any kind of data type in list
print(thislist)
print(thislist[1])
print(thislist[-1])  # -1 refers to the last index
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

thislist[1] = "blackcurrant"  # exchange the item of the given index
print(thislist)

for x in thislist:
    print(x)

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print(len(thislist))

thislist.append("orange")
print(thislist)

thislist.insert(1, "persimon")  # append a new item in the given index
print(thislist)

thislist.pop()  # removes the last item
print(thislist)

del thislist[0]  # deletes the item of a particular index
print(thislist)

#copping a list
mylist = thislist.copy()
print(mylist)
mylist1 = thislist
print(mylist1)

# adding two strings
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

del thislist  # deletes the whole list

listitem = [1, 2, 3, "apple", "banana", "orange"]
print(listitem)
print(listitem[0])  # access an element from the list
# print(listitem[10]) if the given index is out of range it gives the below error:
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# slicing  a list
print(listitem)
print(listitem[2:5])
print(listitem[:4])
print(listitem[2:])
print(listitem[-4:-1])

listitem.append(4)  # inserts an element at the end of the list
print(listitem)

listitem.insert(7, 'mango')  # inserts an element into the particular position
print(listitem)

listitem.insert(-1, 'pineapple')  # inserts an element into the second from last position of the list
print(listitem)

listitem.remove('pineapple')  # removes an particular item
print(listitem)

listitem.pop()
print(listitem)  # removes the last item

listitem.reverse()  # reverse the whole list
print(listitem)

listitem.extend(['grape', 5])  # concatenates a list on to the existing list
print(listitem)

# list comprehensions
numlist = [0, 5, 10]
newnumlist = [x*2 for x in numlist]  # maps through each element
print(newnumlist)


datafile = open('words.txt')

def wDictionaryfin(datafile):
    newdictionary = dict()
    count = 0
    for line in datafile:
        word = line.strip()
        newdictionary[word] = count
        count = count + 1  # after each line it increases its value
    return newdictionary


x = wDictionaryfin(datafile)
print(x)



