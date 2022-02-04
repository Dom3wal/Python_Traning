#Object oriented programing
# CLass ma velke prvni pismeno
# Atributy popsiuji co je objekt nebo co ma za vlastnosci
# Methoda je co objekt umi
from car import Car


car_1 = Car("Chevy","Corvet", 2021, "Blue")
car_2 = Car("Ford","Mustang", 2022, "Red")

car_1.wheels = 2
print(car_1.wheels)

# print(car_1.color)
# car_1.drive()
# car_2.stop()
# print(car_2.model)

print(Car.wheels)  # vypise fdefaultni hodnotu pro danou klasu

Car.wheels = 1
car_1 = Car("Chevy","Corvet", 2021, "Blue")
print(car_1.wheels)
