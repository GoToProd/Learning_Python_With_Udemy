class Calculator():
    def __init__(self):
        pass
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            print(f'Деление на 0 запрещено, это ошибка!')
        else:
            return num1 / num2
        
        
        
calc = Calculator()

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))

operations = input('Выберите операцию: сложение (+), вычитание (-), умножение (*), деление (/). Разрешается использовать знак или слово: ')

if operations == "+" or operations == "сложение":
    result = calc.add(num1, num2)
elif operations == "-" or operations == "вычитание":
    result = calc.subtract(num1, num2)
elif operations == "*" or operations == "умножение":
    result = calc.multiply(num1, num2)
elif operations == "/" or operations == "деление":
    result = calc.divide(num1, num2)
else:
    print(f'ошибка ввода, введите корректные данные')
print(f'Результат: %s' % result)