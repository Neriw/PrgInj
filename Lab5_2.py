Fizra_result = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9,
                21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8,
                24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
Fizra_result10=[]
for i in range(9,len(Fizra_result)):
    Fizra_result10.append(Fizra_result[i])
print("Результаты начиная с 10:")
print(Fizra_result10)
print("Три лучших результата:")
for i in range(3):
    print(max(Fizra_result))
    Fizra_result.pop(Fizra_result.index(max(Fizra_result)))
print("Три худших  результата:")
for i in range(3):
    print(min(Fizra_result))
    Fizra_result.pop(Fizra_result.index(min(Fizra_result)))