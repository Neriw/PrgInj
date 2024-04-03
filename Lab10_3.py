def sloj():
    try:
        a=int(input("Введите число"))
        b=a+2
        print(f"2+{a}={b}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число")
sloj()
sloj()

