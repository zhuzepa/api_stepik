try:
    first = float(input('Введите число: '))
    sign = input('Введите один из знаков (+, -, *, /): ')
    two = float(input('Введите второе число: '))
    if sign == '+':
        print(first + two)
    elif sign == '-':
        print(first - two)
    elif sign == '*':
        print(first * two)
    elif sign == '/':
        print(first / two)
    else:
        print('Ошибка')
except (ZeroDivisionError, ValueError):
    print('Лучше почитай про математику')

