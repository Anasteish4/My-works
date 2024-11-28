while 1 > 0:
    n = int(input('Введите число от 3 до 20: '))
    result: str = ''
    for a in range(1, 21):
        for b in range(a + 1, 21):
            if n % (a + b) == 0 and a != b:
                result += str(a) + str(b)

    print(result)
