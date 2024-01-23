import os


# print(os.name)
# print(os.environ)
# print(os.getcwd())
# print(os.environ['Part'])
# os.rmdir('hello')

filename = input("Pls enter a name for your file:\n")
if os.path.exists(filename):
    print("File exist")
else:
    print("File does not exist")
    