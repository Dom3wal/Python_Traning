# new to python 3.8 ":="

# assigment expressioin

# assigns value to cariables as a part of larger expression

happy = True

print(happy)

#print(happy = True) #cannot work witou walrus operator

print(sad:=False)


# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)
# --------------------------------------------
# dogs = ['Dominik', 'Iza']
# for dog in dogs:
#     print(dog)
# cars = list()

# while car:=input(" What Car do you like? ") != 'quit':
#     cars.append(car)

# for item in dogs:
#     print(item)    

# --------------------------------------------

say = print

say("Hello")


def hello():
    print('Hello')

print(hello) # <function hello at 0x0000019543C66A60> returns address of hello funcion in memory, meni se podle se spustenim programu

hi = hello # odkazuje na stejnou adresu v pameti

hi()
hello()