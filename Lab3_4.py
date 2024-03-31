x = input("Введите предложение на английском\n")
print(f"Длина предложения = {len(x)}")
print(f"В нижним регистре {x.lower()}")
print(f"Кол-во символов a={x.count("a")} e={x.count("e")} i={x.count("i")} o={x.count("o")} u={x.count("u")}")
print(f"Замена 'ugly' на 'beauty' ==> {x.replace("ugly","beauty")}")
if x.startswith("The") and x.endswith("end"):
    print("Строка начинается с 'The' и заканчивается 'end' ")