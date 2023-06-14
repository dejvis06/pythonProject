class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("i took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1


random_monster = Enemy();
print(random_monster.__dict__)
random_monster.take_damage(4)
print(random_monster.__dict__)


class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))


troll = Troll("Troll")
print(troll.__dict__)
troll.take_damage(4)
print(troll.__dict__)
troll.grunt()
