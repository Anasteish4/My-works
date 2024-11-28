#while 1 > 0:
#    n = int(input('Введите число от 3 до 20: '))
#    result: str = ''
#    for a in range(1, 21):
#        for b in range(a + 1, 21):
#            if n % (a + b) == 0 and a != b:
#                result += str(a) + str(b)
#
#    print(result)

import random
def number():
    num = range(3,21)
    rand_num = random.choice(num)
    return rand_num
random_num = number()
print('Число которое выдала плита: ', str(random_num))
result: str = ''
for a in range(1, 21):
    for b in range(a + 1, 21):
        if random_num % (a + b) == 0 and a != b:
            result += str(a) + str(b)

print(result)
