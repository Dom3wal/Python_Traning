# filter funciton creates a collection of elements from an iterable for which a fucntion teruns

# filter(function, iterable)

friends = [("Rachel",20),
            ("Dominik",21),
            ("Adam",17),
            ("Pierd",18)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))

for item in drinking_buddies:
    print(item)

