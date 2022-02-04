# Key and Value they are fast because they use caching

capitals = {"USA":"Woshinton DC",
"Madonna":"Jakson",
"Radek":"Walach"}

capitals.update({"Germany":"Berlin"})

#print(capitals.keys())
print(capitals.items())

capitals.pop("Madonna")

for key,value in capitals.items():
    print(key,value)

