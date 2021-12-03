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