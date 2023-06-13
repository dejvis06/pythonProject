class Kettle(object):
    power_source = "electricity"

    def __init__(self, make, price, another_attribute_private, another_attribute_protected):
        self.make = make
        self.price = price
        self.on = False
        self.__another_attribute_private = another_attribute_private
        self._another_attribute_protected = another_attribute_protected

    def switch_on(self):
        self.on = True

    def get_another_attribute_private(self):
        return self.__another_attribute_private

    @staticmethod
    def print():
        print("Static method called!")

    def print(param=str):
        print("Static method called with param {}".format(param))


kenwood = Kettle("Kenwood", 8.99, "another_attribute_value_private", 'another_attribute_value_protected')
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
print(Kettle("test", 1, "test", "test").power_source)

kenwood.power_source = "oil"
print(kenwood.__dict__)

print()
Kettle.print()
Kettle.print("test")

print()

print(kenwood._another_attribute_protected)

print(kenwood.__dict__.get('_Kettle__another_attribute_private'))
print(kenwood.get_another_attribute_private())
