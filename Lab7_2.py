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