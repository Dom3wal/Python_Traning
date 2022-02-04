class Animal:
    alive = True

    def sleep(self):
        print("This animal is sleeping")
    
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    # Rabbit zdedni vsechny metody Aniaml parrent 
    def run(self):
        print("This rabbit is running")

class Hawk(Animal):
       def fly(self):
        print("This Hawk is flying")

class Fish(Animal):
    pass 

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)

fish.eat()

hawk.fly()

rabbit.run()