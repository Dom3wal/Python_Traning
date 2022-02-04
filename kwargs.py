#**kwargs = keyword arguments= parametr that will pack all arguments into a dictionary useful so that a fucntion can accpet a varying amoutn of keyword arguments

def hello(**kwargs):
    print("Hello " + kwargs['name'] + " " + kwargs['surname'] + ", how you doing?")
    print("You are " + str(kwargs['age']))

hello(name = "Dominik", surname = "Walach", age = 25)

def hello2(**kwargs):
    print("Hello",end = " ")
    for key, value in kwargs.items():
        print(value,end = " ")

hello(name = "Dominik", surname = "Walach", age = 25)
print("-----------")
hello2(name = "Dominik", surname = "Walach", age = 25)