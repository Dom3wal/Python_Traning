import os

# path  = "C:\\Users\\domin\\Desktop\\Test.txt" #\ is a excepa sequence from a strin

# if os.path.exists(path):
#     print("That location Exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("This location doesnt exist")


# try:
#     with open('E:\\THeDolaken\\Python\\test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File has not been find")
# else:
#     print("I have done it")


# Edit files *-----------*

# with open('E:\\THeDolaken\\Python\\test.txt','a') as file:
#     file.write("Hello world\n")
#     file.write("Fuck zou")


# with open('E:\\THeDolaken\\Python\\test.txt') as file:
#     print(file.read())

# # Copy

# import shutil

# # copyfile() = kopiruje obsah souboru
# # copy() = copyfile() + permission mode + destination can be a directory
# # copy2() = copy() + copies metada (file's creation and modification times)

# shutil.copyfile('E:\\THeDolaken\\Python\\test.txt', 'E:\\THeDolaken\\Python\\test2.txt')


# Move files *-----------*
# import os

# source = "E:\\THeDolaken\\Python\\test.txt"
# destination = "E:\\THeDolaken\\Python\\testCopy.txt"

# try:
#     if os.path.exists(destination):
#         print("There is alreay a file")
#     else:
#         os.replace(source,destination)
#         print(source + " was moved")
# except FileNotFoundError:
#     print(source+" Has not been found")

# Delete files *-----------*

import os

os.remove('test.txt') # remove a file
#os.rmdir(path) # delete file or empty folder
# shutil.rmtree(path) # delete files and or folders