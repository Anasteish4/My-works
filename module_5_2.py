class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print('Такого этажа не существует.')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
    def __len__(self):
        return self.number_of_floor
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floor}'


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

h1.go_to(5)
h2.go_to(10)
print(h3)
print(h4)
print(len(h3))
print(len(h4))