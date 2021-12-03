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
