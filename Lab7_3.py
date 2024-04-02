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