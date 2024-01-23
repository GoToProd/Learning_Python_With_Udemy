# f = open('test.txt', 'r')
# print(*f)

# Methode 1
# f = open('test.txt', 'r')
# f.close()

# Method 2
# f = open('test.txt', 'r')
# try:
#     pass
# except:
#     pass
# finally:
#     f.close() 

# Method 3
# with open('test.txt', 'r') as f:
#     pass


# f = open('test.txt', 'r')
# print(f.read (10))

# f = open('test.txt', 'r')
# f.readlines(1)
# f.readlines(1)
# f.readlines(1) 
# print(f.readlines())

# f = open('test.txt', 'w')
# f.write('Hello, my dear Python!\n')
# f.close()
# f =  open('test.txt', 'r')
# print(*f)
# f.close() 

# import os
# os.rename('test.txt','abc.txt')


poem = """ 
I want to say you about
BEST RULES OF PYTHON
but i am not learning it
and i dont know rules
"""

f = open('words.txt', 'w')
f.write(poem)
f.close()
f = open('words.txt', 'r')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()