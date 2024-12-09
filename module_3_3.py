#Задача "Распаковка"
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(89)
print_params(37,8)
print_params(False,7,'it is work!')
print_params(b=25)
print_params(c=[1, 2, 3])

#Распаковка параметров
values_list = [2, False, 'smile)']
values_dict = {'a': 2024, 'b': '-->2025', 'c': True}
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры

values_list_2 = ['The New Year is coming soon', 2025]
print_params(*values_list_2,42)
print_params(*values_list_2,'happy!!!') 