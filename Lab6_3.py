str=input("наберите случайно 15 цифр")
def number(str):
    chastota = {}
    for i in str:
        i = int(i)
        chastota[i] = chastota.get(i, 0) + 1
    sortch = sorted(chastota.items(), key=lambda item: item[1])
    top = dict(sorted(sortch[-3:]))
    return top
print(number(str))