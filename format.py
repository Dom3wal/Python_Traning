#str.format () optional method that gives users more controll when displaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal,item))
print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item)) #positional argument
print("The {animal} jumped over the {item}".format(animal = "animal",item = "item")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Domka"
print("Hello MY name is {}".format(name))
print("Hello MY name is {:10}. Nice to meet you".format(name))
print("Hello MY name is {:<10}. Nice to meet you".format(name))
print("Hello MY name is {:>10}. Nice to meet you".format(name))
print("Hello MY name is {:^10}. Nice to meet you".format(name))

number = 3.141592

print("The number pi is {:.2f}".format(number))

number2 = 10000

print("The number pi is {:,}".format(number2))
print("The number pi is {:b}".format(number2)) #binary
print("The number pi is {:x}".format(number2)) #hex
print("The number pi is {:X}".format(number2)) #hex
print("The number pi is {:E}".format(number2)) # scientific

name = "PYTHON DEVELOPER (IMAGE PROCESSING)"
# print(name.capitalize())

# questions = {
#     "Who is Dominik? ":"A",
#     "Jak se mosz? ":"B",
#     "Je Zeme kulata? ":"C",
#     "Je Iza pierda? ":"A"
# }

# options = [["A. Dominik", "B. Radek","C. Iza"],
#            ["A. Dobrze", "B. Eszcze lepi","C. Nanic"],
#            ["A. Nima", "B. Hranto","C. Je"],
#            ["A. Ja", "B. Ni","C. Mozna"]]

# num=0
# for key in questions:
#     print(key)
#     for item in options[num]:
#         print(item)
#     num +=1