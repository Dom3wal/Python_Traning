class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal Hunts!")
        return self # neded for method channing

    def eat(self):
        print("Im eating")
        return self # neded for method channing


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit=Rabbit()
hawk = Hawk()
fish = Fish()

fish.hunt()
fish.flee()

# method channing

hawk.eat()\
.hunt()

