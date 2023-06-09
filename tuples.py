t = 'a','b','c'
print(t)

t = ('a','b','c')
print(t)

x, y, z = t
print(x)
print(y)
print(z)

for touple in enumerate("abcdefgh"):
    index, value = touple
    print(touple)
    print(index, value)