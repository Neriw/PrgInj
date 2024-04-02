try:
    with open("Task5.txt","r", encoding='utf-8') as file:
        content=file.read()
        print(content.replace("-",""))
except Exception as e:
    print("Ошибка: ", str(e))