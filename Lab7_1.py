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