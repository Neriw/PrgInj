
# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил(а):
- Михайлов Александр Валерьевич
- ИНО ЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language

    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")

City1 = City('Москва', "Россия", 'Русский')
City2 = City("Берлин", "Германия", "Немецкий")
City3 = City("Париж", "Франци", "Французксий")
City1.inf()
City2.inf()
City3.inf()
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_1.png)
### Выводы
В данном коде создан класс City с атрибутами name,country,language и методом inf
  
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language

    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")
    def clear(self):
        self.name=""
        self.country=""
        self.language=""
City1 = City('Москва', "Россия", 'Русский')
City1.inf()
City1.clear()
City1.inf()
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_2.png)
### Выводы
В данном коде создан класс City с атрибутами name,country,language и методоми inf, clear
  
## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language
    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")
class Obl(City):
    def __init__(self, name, country, language, obl):
        super().__init__(name, country, language)
        self.obl=obl
    def infobl(self):
        print(f"Область = {self.obl}")
City1 = City("Москва", "Россия", "Русский")
City1.inf()
City2 = Obl("Омск", "Россия", "Русский","Омская")
City2.inf()
City2.infobl()

```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_3.png)
### Выводы
В данном коде создан класс реализовано наследование класса City классом Obl
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class City:
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language
    def inf(self):
        return f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}"

City1 = City("Москва", "Россия", "Русский")
print(City1.name)
print(City1.inf())

```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_4.png)
### Выводы
В данном коде реализвана инкапсуляция
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
```python
class obj:
    def inf(self):
        pass
class City(obj):
    def __init__(self, name, country, language):
        self.name = name
        self.country = country
        self.language = language
    def inf(self):
        print(f"Информация о городе:\nНазвание: {self.name}\nСтрана: {self.country}\nЯзык: {self.language}")
class StreetIn(obj):
    def __init__(self, name, street):
        self.name=name
        self.street=street
    def inf(self):
        print(f"Город = {self.name}\nУлица = {self.street}")
City1 = City("Москва", "Россия", "Русский")
City1.inf()
City2 = StreetIn("Омск", "Ленина")
City2.inf()
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_8/pic/Lab8_5.png)
### Выводы
В данном коде реализван полиморфизм
  
## Общие выводы по теме
В этой самостоятельной работе была изучены основы объектно-ориентированного программирования
