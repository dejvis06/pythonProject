parrot = "Norwegian Blue"
for character in parrot:
    print(character)

shopping_list = ["milk", "pasta", "eggs", "spam", "bread"]
for item in shopping_list:
    if item == "spam":
        continue
    else:
        print(item)

print("-----------")

for item in shopping_list:
    if item == "spam":
        break
    else:
        print(item)
