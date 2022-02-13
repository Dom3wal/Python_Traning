# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”


class Bird():
    def __init__(self,name):
        self.name = name
    
    def walk(self):
        print("This " + self.name + " is walking")

    def talk(self):
        print("This duck is qwuacking")


class Duck(Bird):
    pass


class Chicken(Bird):

    def walk(self):
        print("This " + self.name +"is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

bird = Bird("Bird")
duck = Duck("Dauck")
chicken = Chicken("Chaicken")
person = Person()

person.catch(chicken)

# print(duck.walk())