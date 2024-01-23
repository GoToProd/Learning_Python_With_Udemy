# class Person:
#     name = "Tom"
    
#     def display_name(self):
#         print(f"Ваше имя: {self.name}")
        
# person1 = Person()
# person1.display_name()

# person2 = Person()
# person2.name = "Sam"
# person2.display_name()

class Person:
    def __init__(self, name, age):
        self.name = name
        name = 'Anonimouse'
        self.age = age
        age = 0
        
    def display_info(self):
        print(f'Hello my name is {self.name} and my age is {self.age}')

person1 = Person('Dias', 25)
person1.display_info()

person2 = Person('Any', 0)
person2.name = "Sam"
person2.age = 18
person2.display_info()

person1 = Person('Боб', 18)
person1.display_info()
