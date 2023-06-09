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
