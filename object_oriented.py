class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

print()

kenwood.price = 12.75
print(kenwood.price)

print()

# kenwood.switch_on()
print(kenwood.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print()

print(kenwood.power_source)
print(Kettle("test", 1).power_source)

kenwood.power_source = "oil"
print(kenwood.__dict__)