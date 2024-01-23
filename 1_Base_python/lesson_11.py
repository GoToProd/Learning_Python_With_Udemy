# string = "5"
# number = int(string)
# print(type(string))
# print(type(number))

# string = "Hello, world!"
# number = int(string)
# print(number)

# try:
#     number  = int(input("Введите число: \n"))
#     print(f'Ваша цифра: {number}\n')
# except ValueError:
#     print(f'Вводите число, а не слово! {number}')

# try:
#     number1  = int(input("Введите число 1: \n"))
#     number2  = int(input("Введите число 2: \n"))
#     print(f'результат деления {number1/number2}\n')
# except NameError:
#     if int(number1) : 
#         print(f'Вводите число, а не слово! {number1}')
#     elif int(number2) & number2 > 0 :
#         print(f'Вводите число, а не слово! {number2}')
# except ZeroDivisionError:
#     print(f'На 0 не делят!!!')
# except ValueError:
#     print(f'Ну ты совсем дурак, нет?')
# except Exception:
#     print(f'ошибка!')

def input_number():
    while True:
        try:
            res = int(input(''))
            return print(f"Вы ввели {res}")
        except:
            print(f"\n Дурак? число введи!")
            continue
        
input_number()