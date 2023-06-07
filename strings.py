greeting = "Hello"
name = "Bruce"

print(greeting + " " + name)

# name = input("Please enter your name: ")
# print(greeting + ' ' + name)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[0:6])
print(parrot[:6])
print(parrot[10:])
print(parrot[:])
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,111,111,111,111"
print(number[1::4])

today = "friday"
print("day" in today)
print("not_in" in today)

age = 24
print("My age is: " + str(age))
print("My age is: {0}".format(age))
print("First param: {0}, second param: {1}".format(age, 25))
