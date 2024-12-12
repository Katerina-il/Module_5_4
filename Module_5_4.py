"""     Домашняя работа по уроку "Различие атрибутов класса и экземпляра"       """
"""   Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__.   """


class House:
    houses_history = []
    
    def __new__(cls, *args, **kwargs):
    	cls.houses_history.append(args[0])
    	print(*cls.houses_history)
    	return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        """  Developer - не только разработчик. Строительство здания """
        self.name = name
        self.number = number_of_floors  # количество этажей
       
  
    def go_to(self, new_floor):

        if new_floor > self.number or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number}"

    def __len__(self):
        return self.number

    def __eq__(self, other):
        return self.number == other.number

    def __add__(self, value):  # увеличивает кол - во этажей на переданное значение value, возвращает сам объект self.
        self.number += value
        return self

    def __radd__(self, value):
        return self + self.number + value

    def __iadd__(self, value):  # - работают так же как и __add_(возвращают результат его вызова)
        # self.number += value
        return add

    def __lt__(self, other):
        """  для оператора меньше < """
        if isinstance(other, (House)) and isinstance(other.number, (int)):
            return self.number < other.number
        else:
            print("Невозможно сравнить разные данные")



    def __le__(self, other):
        """  для оператора меньше или равно <= """
        if isinstance(other, (House)) and isinstance(other.number, (int)):
            return self.number <= other.number
        else:
            print("Невозможно сравнить разные данные")

    def __gt__(self, other):
        """   для оператора больше > """
        if isinstance(other, (House)) and isinstance(other.number, (int)):
            return self.number > other.number
        else:
            print("Невозможно сравнить разные данные")

    def __ge__(self, other):
        """  для оператора больше или равно >=  """
        if isinstance(other, (House)) and isinstance(other.number, (int)):
            return self.number >= other.number
        else:
            print("Невозможно сравнить разные данные")

    def __ne__(self, other):
        """  для неравенства != """
        if isinstance(other, (House)) and isinstance(other.number, (int)):
            return self.number != other.number  # должны возвращать результаты сравнения
        else:
            print("Невозможно сравнить разные данные")
            
    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')
            
          
          
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)



# Удаление объектов

del h2
del h3



print(House.houses_history)