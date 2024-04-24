import math

#Возвести в квадрат
def function1():
    print('Я function1 из Module2 (Квадрат):')
    a = int(input('Введите число a: '))
    x = a ** 2
    print('Число "a" в квадрате =', x)


# function1()

# Возвести в любую степень
def function2():
    print('Я function2 из Module2 (Степень):')
    a = int(input('Введите число a: '))
    b = int(input('Введите число b: '))
    x = a ** b
    print('Число "a" в степени "b" =', x)


# function2()

# Квадратный корень
def function3():
    print('Я function3 из Module2 (Квадратный корень):')
    a = int(input('Введите число a: '))
    x = math.sqrt(a)
    print('Квадратный корень числа "a"  =', x)


# function3()


# Логарифм по основанию 2
def function4():
    print('Я function4 из Module2 (Логарифм):')
    a = int(input('Введите число a: '))
    x = math.log2(a)
    print('Логарифм "a" по основанию 2 =', x)


# function4()