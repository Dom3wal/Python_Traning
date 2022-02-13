#reduce recycle values in an interable, until single value remains. performs function to first two elements!
# reduce(function,iterable)
letter = ["H","E","L","L","O"]

import functools

word = functools.reduce(lambda x,y:x+y,letter)
# how its working Takes H and E = "HE","L",...
#then "HEL","L"...
print(word)

factorial =[5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorial)

print(result)