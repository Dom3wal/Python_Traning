# map() apllies a focntion to each item in an iterable

# map(function, iterable)

store = [("shirt",20.00),
        ("pants", 30.00),
        ('jacket',50.00),
        ("socks",10.00)]

to_euros = lambda data: (data[0],round(data[1]*0.82,5))

store_euros = list(map(to_euros,store)) # list si here to deisplzy it latter


for item in store_euros:
    print(item)

