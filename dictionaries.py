vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100'
}

print(vehicles)

dream_car = vehicles['dream']
print(dream_car)

roadster = vehicles.get('roadster')
print(roadster)

print('dream' in vehicles)

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

print('--------------')

vehicles.__delitem__('starfighter')
print(vehicles)

del vehicles['dream']
print(vehicles)

result = vehicles.pop('f1', None)
print(result)

result = vehicles.pop('f1', "Doesnt exist!")
print(result)

result = vehicles.pop('roadster', "Doesnt exist!")
print(result)

other_vehicles = {
    'mercedes': 'c-class',
    'audi': 'A7'
}

vehicles.update(other_vehicles)
print(vehicles)

updated_vehicles = {
    'mercedes': 'b-class'
}
vehicles.update(updated_vehicles)
print(vehicles)

array = vehicles.values();
print(array)