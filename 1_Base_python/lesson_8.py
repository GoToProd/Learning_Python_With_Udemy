import numpy as np


# z = np.zeros(10)
# print(z)

# z = np.ones(10)
# print(z)

# z = np.full(10,2.5)
# print(z)


# z = np.array([1,2,3])
# print(z)

# z = np.arange(10,50)
# print(z)

# z = np.ones((10,10))
# z[1:-1,1:-1]=0
# print(z)

# z = np.ones(5)
# print(z*4)

print('1 question:')
zero_vektor = np.zeros(10)
print(zero_vektor, '\n\n')

print('1.2 question:')
vektor_3x3 = np.zeros((3,3))
print(vektor_3x3,"\n\n")

print('2 question:')
array_vektor = np.array([1,2,3,4,5,6,7,8,9,10])
array_vektor_second = np.arange(1,10)
print(array_vektor)
print(array_vektor_second, '\n\n')

print('3 question:')
matrix_vektor = np.ones((10, 10))
matrix_vektor[1:-1,1:-1]=0
print(matrix_vektor, '\n\n')

print('4 question:')
array_vektor = np.arange(1,11)
reverse_array_vektor = np.flip(array_vektor)
# second variable
reversed_array = np.arange(10,0,-1)
print(reversed_array,)
print(reverse_array_vektor, '\n\n')

print('5 question:')
vektor_line1 = np.array((1,2,3))
vektor_line2 = np.arange(1,4)
print(vektor_line1*2)
print(vektor_line2*2)
print('\n\n')

print('Bonus level:')
x = np.array((1,2,3))
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    
    return s

print('сигмовидная функция равна: ', sigmoid(x), '\n\n')


data = [1, 2, 3]
for y in data:
    print(sigmoid(y))
print('- Второй вариант \n\n')

q:float = 1
w:float = 2
e:float = 3
data2 = [q, w, e]
for y in data2:
    print(sigmoid(y))
print('- Третий вариант\n\n')