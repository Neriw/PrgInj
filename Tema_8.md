
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
В программе считается кол-во букв, слов и строк
  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. • Запрещенные слова: hello email python the exam wor is
### • Предложение для проверки:
### Hello, world! Python IS the programming language of thE future. My EMAIL is....
### PYTHON is awesome!!!!
### • Ожидаемый результат:
### *****, ***ld! ****** ** *** programming language of *** future. My ***** **....
### ****** ** awesome!!!!
```python
word=["hello", "email", "python", "the", "exam", "wor", "is"]
try:
    with open("input.txt","r", encoding='utf-8') as file:
        content=file.read()
        low = content.lower()
        for i in range(len(word)):
            low=low.replace(word[i],"*")
        print(low)
except Exception as e:
    print("Ошибка: ", str(e))
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_4.png)
### Выводы
Программа заменяет все запрещенные слова *, в зависимости от кол-ва символов на такое же количесвто *
  
## Самостоятельная работа №5
### Прочитать информацию из файла и удалить все символы "-"
```python
try:
    with open("Task5.txt","r", encoding='utf-8') as file:
        content=file.read()
        print(content.replace("-",""))
except Exception as e:
    print("Ошибка: ", str(e))
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_5_1.png)
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_5_2.png)
### Выводы
В данном коде удаляются все символы "-"
  
## Общие выводы по теме
В этой самостоятельной работе была изучена работа с файлами (ввод, вывод)
