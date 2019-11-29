from pow import my_pow
from my_sqrt import sqrt

print("Очень крутой калькулятор!")
a = input("Введите а =")
b = input("Введите b =")

# TODO высти операторы
print("pow, возведение a в степень b")
print("sqrt, корень a-ой степени из числа b")
operator = input("Оператор =")
c = None  # реузльтат сюда

# TODO вычисления резултата
if operator == "pow":
    c = my_pow(a, b)

if operator == "sqrt":
    c = sqrt(a, b)
