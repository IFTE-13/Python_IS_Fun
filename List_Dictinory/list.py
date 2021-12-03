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


