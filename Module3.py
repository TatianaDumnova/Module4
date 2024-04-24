from math import factorial


# Округление
def function1():
    print('Я function1 из Module3 (Округление):')
    a = float(input('Введите число "a": '))
    x = round(a, 2)
    print('Округление числа "a" (2 знака после запятой)  =', x)


# function1()


# Факториал
def function2():
    print('Я function2 из Module3 (Факториал):')
    a = int(input('Введите число "a": '))
    x = factorial(a)
    print('Факториал числа "a"  =', x)


# function2()


# Фибоначчи
def function3():
    print('Я function3 из Module3 (Фибоначчи):')
    a = int(input('Введите число "a": '))
    fib1 = 0
    fib2 = 1
    for i in range(2, a):
        fib1, fib2 = fib2, fib1 + fib2
    if a == 1:
        fib2 = 0
    print('Значение "a" в последовательности Фибоначчи =', fib2)


# function3()
