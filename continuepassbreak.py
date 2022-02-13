
# # continue = skips the cone after in, but continues the loop, unlike break
# for i in range(0,20):
#     print(i)
#     if i == 10:
#         print("i = 10")
#         continue

for j in range(0,10):
    for i in range(0,20):
        print(i)
        if i == 10:
            print("i = 10")
            break
    print("I have broke is loop")

print("Im out of the loops")