#класс-декоратор my_dec
class my_dec:
    def __init__(self, func): # Инициализация метода конструктора с функцией func
        self.func = func
    def __call__(self, *args, **kwargs):
        print(f'Декоратор до "{self.func.__name__}"')
        result = self.func(*args, **kwargs)  # Выполнение функции с переданными аргументами
        print(f'Декоратор после "{self.func.__name__}"')
        return result
# Декорирование функций slojstrok и umnoj с помощью декоратора my_dec
@my_dec
def slojstrok(a, b):
    return a + b  # сложение
@my_dec
def umnoj(a, b):
    return a * b  # умножение
x = int(input('Введите первое чило: '))
y = int(input('Введите второе число: '))

print(slojstrok(x, y))
print(umnoj(x, y))