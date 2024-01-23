# # def hello_world():
# #     print ("Hello World")
    
# # # hello_world()
# # # hello = hello_world()

# # # def hello_world2():
# # #     def internal():
# # #         print ("Hello World second version")
# # #     return internal

# # # hello2 = hello_world2()
# # # print (hello2)

# # # def say_smt(func):
# # #     func()
    
# # # say_smt(hello_world)

# # def log_dec(func):
# #     def wrap():
# #         print (f'Calling a func {func}')
# #     func()
# #     print (f'Ending a func {func}')
# #     return wrap

# # wrapped = log_dec(hello_world)
# # wrapped()

# # @log_dec
# # def hello():
# #     print (f'Hello my friend')
    
# # hello()


# from timeit import default_timer as ti 
# import math
# import time
# from functools import wraps

# # def measure_time(func):
# #     @wraps(func)
# #     def inner(*args, **kwargs):
# #         start = ti()
# #         func(*args, **kwargs)
# #         end = ti()
# #         print (f'Function {func.__name__} took {end - start} for execution')
# #     return inner


# # @measure_time
# # def factorial(num):
# #     #time.sleep(5)
# #     print (math.factorial(num))
    
# #factorial(4)

# # help(factorial)

# def decotator(F):
#     def wrapper(*args):
#         z = 1
#         for i in args:
#             z*=i
#         print(z)
#     return wrapper

# @decotator
# def func(*args):
#     time.sleep(2)
#     print(f'The number what you enter {args}')
    
# func(1,2,3,4,5,6,7,8)



class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
        
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age in range(1,100):
            self.__age = age
        else:
            print(f'Impossible age {age}. Entering age in range 1 - 100.')
            
    def display(self):
        print("Name:", self.__name,"\tAge:", self.__age )
        
        
        
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        
    def yearly_salary(self):
        return (self.pay * 12 ) + self.bonus
    
class Employee(Person):
    def __init__(self,name,age,company,pay,bonus):
        Person.__init__(self,name,age)
        self.salary = Salary(pay, bonus)
        self.company = company
        
    def display_info(self):
        Person.display(self)
        print('Company', self.company)
        
    def total_salary(self):
        return self.salary.yearly_salary()
    
class Student(Person):
    def __init__(self,name,age,university):
        Person.__init__(self,name,age)
        self.university = university
        
    def display_info(self):
        print('Student',self.university)
        
people = [Person('Tom', 23), Student("Bob", 19, 'Harward'), Employee('Sam', 35, 'Google', 10000000, 100000)]    

for person in people:
    person.display()
    print()