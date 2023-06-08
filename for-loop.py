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

print("-----------")

found_at = None
item_to_find = "pasta1"

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("Found at index {}".format(found_at))
