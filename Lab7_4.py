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