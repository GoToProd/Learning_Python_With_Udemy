# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def name(self):
#         return self.name
    
#     def display_info(self):
#         print(f'Name: {self.name}')
        

# class Employee:
#     def __init__(self, name):
#         self.name = name
        
#     def display_info(self):
#         print(f'Name: {self.name}')
    
#     def work(self):
#         print(f'Name: {self.name}')

class Person:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    def display_info(self):
        print(f'Name: {self.__name}')
        

class Employee(Person):
    def work(self):
        print(f'Name: {self.name} works')
        
tom = Employee("Tom")
print(tom.name)
tom.display_info()
tom.work()