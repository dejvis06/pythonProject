farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

print()

farm_animals.add('dog')
print(farm_animals)

print()

farm_animals.discard('dog')
farm_animals.remove('hen')
print(farm_animals)

print()

wild_animals = {'boar', 'wolf'}
print(farm_animals.union(wild_animals))
