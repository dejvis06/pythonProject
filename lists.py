computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

for part in computer_parts:
    print(part)

print(computer_parts[0])
print(computer_parts[0:3])
print(computer_parts[-1])

computer_parts.append("another part")
print(computer_parts)

print(computer_parts.index("another part"))

for index, part in enumerate(computer_parts):
    print("Index is: {0}, part: {1}".format(index, part))

computer_parts.remove("another part")
print(computer_parts)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)

computer_parts.sort()
print(computer_parts)

computer_parts.sort(reverse=True)
print(computer_parts)

sorted_computer_parts = sorted(computer_parts)
print(sorted_computer_parts)

computer_parts[3:] = "trackball"
print(computer_parts)

computer_parts[:2] = "test"
print(computer_parts)

del computer_parts[5:]
print(computer_parts)

del computer_parts[:4]
print(computer_parts)

del computer_parts[0]
print(computer_parts)

computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
for index, part in enumerate(reversed(computer_parts)):
    print(index, part)

nested_lists = [computer_parts]
for nested_list in nested_lists:
    print(nested_list)
    for element in nested_list:
        print(element)