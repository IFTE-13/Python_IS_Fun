# Write a program that reads data.txt and prints only the words with more than 20 characters.
data = open('data.txt')

for line in data:
    for word in line.split():
        if len(word) >= 20:
            print(word)


# Write a function that reads data.txt and prints only the words that has no character e
def has_no_e(z):
    for lines in data:
        for words in lines.split():
            if z not in words:
                print(words)


has_no_e("e")

# Write a function that takes a list of numbers and returns the cumulative sum; that is a new list where the ith
# element is the sum of the first i + 1 elements form the original list.
num = [1, 2, 3]
final = []
total = 0
for x in num:
    total += x
    final.append(total)
print(final)
