
# args are packed to the tuple()  = ordered unchengable, need to be converted to list
def hello(*args):
    print(args)
    
    for item in args:
        print(item)

    for i in args:
        print(" ")
        for y in i:
            print(y)

hello("world","Hello", "Dominik")