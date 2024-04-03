class MyExc(Exception):
    pass
# проверки на тип - строка
def positive_number(n):
    try:
        if type(n)!=type("str"):  # проверка на тип - строка
            raise MyExc(f'{n} не строка')
        print(f'Строка - : {n}')  # вывод строки
    except MyExc as e:
        print(f'Поймано исключение: {e}')  # информация об исключении
# если строка не содержит только цифры
def only_letters(s):
    try:
        if not s.isalpha():  #содержит ли строка только буквы
            raise MyExc(f'{s} содержит не только буквы')
        print(f'Введена строка только из букв: {s}')  # вывод строки, состоящей только из букв
    except MyExc as e:
        print(f'Поймано исключение: {e}')
test_str = input('Введите строку ')
positive_number(test_str)
test_string = input('Введите строку ')
only_letters(test_string)