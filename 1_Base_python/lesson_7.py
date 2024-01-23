import math


#возведение чисоа в степнь
n1 = math.pow(2,4)
print(n1)
print(type(n1))

n2 = 2**4
print(n2)
print(type(n2))


#квадратный корень числа
a = math.sqrt(272)
print(a)
print(type(math.sqrt(16)))

#ближайшее целое число в большую сторону
print(math.ceil(a))
print(type(math.ceil(a)))

#ближайшее целое число в меньшую сторону
print(math.floor(a))
print(type(math.floor(a)))

#перевод из радиан в градусы
print(math.degrees(a))
print(type(math.degrees(a)))

#из градусов в радианы
print((math.radians(180)))

#синусы и косинусы
b = math.cos(math.radians(60))
print((type(b)), (b))
print(math.sin(math.radians(90)))
print(math.tan(math.radians(0)))
