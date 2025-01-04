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
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        return False
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        return False
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        return False
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        return False
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
            return self
        return NotImplemented
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

h1.go_to(5)
h2.go_to(10)
#дополнение к первоначальному коду
print('     ')
print(h3)
print(h4)
print(len(h3))
#второе дополнение к первоначальному коду
print('     ')
print(h3)
print(h4)

print(h3 == h4) #eq

h3 = h4 + 10 #add
print(h3)
print(h3 == h4)

h3 += 10 #iadd
print(h3)

h4 = 10 + h4 #radd
print(h4)

print(h3 > h4) #gt
print(h3 >= h4) #ge
print(h3 < h4) #lt
print(h3 <= h4) #le
print(h3 != h4) #ne