# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.age = 1
        
#     def display_info(self):
#         print(f'Name: {self.name} and age: {self.age}')
        
# tom = Person("Tom")
# tom.name = "Dias"
# tom.age = "-123"
# tom.display_info()

class Person:
    def __init__(self,name):
        self.__name = name
        self.__age = 1
        
    def set_age(self,age):
        if 1 < age < 110:
            self.__age = age
        else:
            print(f'Impossible age!!!')
            
    def get_age(self):
        return self.__age
        
    def get_name(self):
        return self.__name
    
    def display_info(self):
        print(f'Name: {self.__name} and age: {self.__age}')
        
        
        
        
tom = Person("Tom")
# tom.name = "Dias"
# tom.age = "-123"
tom.display_info()