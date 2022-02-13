# list comprehension = a way to create a new list with less syntax
# can mimic a certain lambda function
# list = [expression for a item in iterable]

# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

#insted we can use

squares = [i*i for i in range(1,11)]

print(squares)
# --------------------------------------------
students = [100,90,80,60,50,40,30,20,10]

passed_students = list(filter(lambda data: data >= 60,students))

for item in passed_students:
    print(item)