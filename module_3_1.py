calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    lenght = len(string)
    upp = string.upper()
    low = string.lower()
    return (lenght, upp, low)
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    for item in list_to_search:
        if item.lower() == string_lower:
            return True
    return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
