# Printing Hello world
print("Hello World")

# Variable declaration
a = 200
b = 300

# if else

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# For Loop
for x in range(10):
    print(x)  # prints form 0 to 9


# function
def my_function():
    x = 10
    print("Value inside function: ", x)


x = 20
my_function()
print("Value outside function: ", x)

# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time(second,minute) per mile?
# What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).
minutes = 43
seconds = 30
totalTime = minutes + seconds / 60

speedPerHour = 10 * 60 / totalTime  # Kilometer per hour
print(speedPerHour)

speedInMile = speedPerHour / 1.61  # Mile per hour
print(speedInMile)

speedInTime = 60 / speedInMile
print("Avg time per mile in: ", speedInTime, "min")

# The volume of a sphere with radius r is 4/3 p r3. What is the volume of a sphere with radius 5?
r = 5
p = 3.1416
volume = (4 / 3) * p * (5 ** 3)
print(volume)

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
cost = 24.95
discount = cost * .4
finalPrice = cost - discount
totalBookPrice = finalPrice * 60

shippingCost = 3 + (0.75 * 59)
totalBill = totalBookPrice + shippingCost
print("Total Bill: $", totalBill)


# Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.
# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces
# so that the last letter of the string is in column 70 of the display.

def right_justify(name):
    x = len(name)
    print((70-x) * "\n")
    for n in name:
        print(n)

right_justify("allen")

# Write a function that draws a grid
def grids(area, unit):
    for _ in range(area):
        print(("+" + "- " * unit) * area + "+")
        for _ in range(unit):
            print(("|" + "  " * unit) * area + "|")
    print(("+" + "- " * unit) * area + "+")


grids(2, 5)