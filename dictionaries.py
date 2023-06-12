vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100'
}

print(vehicles)

dream_car = vehicles['dream']
print(dream_car)

roadster = vehicles.get('roadster')
print(roadster)

print('--------')

for key in vehicles:
    print(key)

for key in vehicles:
    print(key, vehicles[key])

for key, value in vehicles.items():
    print(key, value, sep=', ')

print('--------------')

vehicles['starfighter'] = "Lockheed F-104"
print(vehicles['starfighter'])
vehicles['starfighter'] = "Lockheed F-1041"
print(vehicles['starfighter'])

vehicles.__delitem__('starfighter')
print(vehicles)

del vehicles['dream']
print(vehicles)

result = vehicles.pop('f1', None)
print(result)