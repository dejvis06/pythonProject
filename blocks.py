name = input("Please enter your name: ")
age = int(input("Please enter your age {0}: ".format(name)))

print(age)

if age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
elif age == 901 or age == 902:
    print("Sorry, Yoda, you are still dead")
elif age >= 903 and age <= 905:
    print("Ok Yoda just stop trying...")
elif age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18 - age))





