from pow import my_pow

print("Очень крутой калькулятор!")
a = input("Введите а =")
b = input("Введите b =")

# TODO высти операторы
print("pow, возведение a в степень b")

operator = input("Оператор =")
c = None  # реузльтат сюда

# TODO вычисления резултата
if operator == "pow":
    c = my_pow(a, b)
if operator == "minus":
    c = my_minus(a, b)

if operator == "sqrt":
    c = sqrt(a, b)

print("Результат = {}".format(c))
