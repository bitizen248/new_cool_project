from minus_func import my_minus
from my_sqrt import sqrt
from pow import my_pow
from division import division

print("Очень крутой калькулятор!")
a = input("Введите а =")
b = input("Введите b =")

# TODO высти операторы
print("pow, возведение a в степень b")
print("sqrt, корень a-ой степени из числа b")

print('division, деление a на b')
operator = input("Оператор =")
c = None  # реузльтат сюда

# TODO вычисления резултата
if operator == "pow":
    c = my_pow(a, b)
if operator == "minus":
    c = my_minus(a, b)
if operator == 'division':
    c = division(a, b)
if operator == "sqrt":
    c = sqrt(a, b)

print("Результат = {}".format(c))
