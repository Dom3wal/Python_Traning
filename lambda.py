# written in one line with labda, one use funcsion

# def double(x):
#     return x*2

# print(double(5))

double = lambda x:x*2 # parametr x and expression x*2
print(double(5))

age_check = lambda age: True if age > 18  else False
print(age_check(15))