# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
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
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово.
```python
try:
    with open("file.txt","r", encoding='utf-8') as file:
        content=file.read()
        Mylist=content.split()
        print(f"Кол-во слов в статье = {len(Mylist)}")
        slovar={}
        for i in Mylist:
            slovar[i]=slovar.get(i,0)+1
        SamChastoe = sorted(slovar.items(), key=lambda item: item[1])
        Slovo=dict(SamChastoe[-1:])
        for a,b in Slovo.items():
            print(f"Самое частое слово '{a}' Встречается {b} раз(а) в тексте")
except Exception as e:
    print("Ошибка: ", str(e))
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_1_1.png)
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_1_2.png)
### Выводы
В данном коде на вход поступает информация из текстового файла, считается количество слов в текстовом файле и определяется самое часто встречающееся слово.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль.
```python
try:
    file=open("Stock.txt","a", encoding='utf-8')
    Prise=int(input("Введите цену товара "))
    Kol=int(input("Введите кол-во товара "))
    Sum=Prise*Kol
    file.write(f"Цена товара - {Prise}\nКол-во товара - {Kol}\nСумма - {Sum}\n")
    file.close()
    file = open("Stock.txt", "r", encoding='utf-8')
    content = file.read()
    print(content)
except Exception as e:
    print("Ошибка: ", str(e))
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_2_1.png)
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_2_2.png)
### Выводы
Программа позволяет вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль.
  
## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### • Текст в файле:
### Beautiful is better than ugly.
### Explicit is better than implicit.
### Simple is better than complex.
### Complex is better than complicated.
### • Ожидаемый результат:
### Input file contains:
### 108 letters
### 20 words
### 4 lines
```python
try:
    with open("Task3.txt","r", encoding='utf-8') as file:
        content=file.read()
        Mylist=list(content)
        j,k=1,0
        for i in Mylist:
            if i!=" " and i!='\n' and i!=".":
                k=k+1
            if i=='\n':
                j=j+1
        print(f"Кол-во букв {k}")
        print(f"Кол-во слов {len(content.split())}")
        print(f"Кол-во строк {j}")
except Exception as e:
    print("Ошибка: ", str(e))
```
### Результат.
![Меню](https://github.com/Neriw/PrgInj/blob/%D0%A2%D0%B5%D0%BC%D0%B0_7/pic/Lab7_3.png)
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
