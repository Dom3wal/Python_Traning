# students=['Dominik','Iza', 'Radek', 'Banan']

# key or reverse arguments to list fort sort METHOD

# students.sort(reverse=True)

# for tuple
students=('Dominik','Iza', 'Radek', 'Banan')
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)
    
# --------------------
# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
# students.sort(key=age)                                       # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list
# KEy musi byt function object
for i in sorted_students:
    print(i)

# --------------------