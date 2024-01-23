class Soda:
    def __init__(self, additive):
        if isinstance(additive, str):
            self.additive = additive
        else:
            raise ValueError("Ошибка: Добавка должна быть словом")

    def show_my_drink(self):
        if self.additive:
            print("Газировка и", self.additive)
        else:
            print("Обычная газировка")


# Создаем экземпляр класса Soda с указанной добавкой
try:
    additive = input("Введите добавку к газировке: ")
    if additive.isalpha():
        soda = Soda(additive)
        # Выводим выбранный напиток
        soda.show_my_drink()
    else:
        print('Это не слово!')
except ValueError as e:
    print(e)
