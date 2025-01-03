def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
inner_function() # при попытке вывести данную функцию будет ошибка, так как она существует
# только  в пространсве "test_function"