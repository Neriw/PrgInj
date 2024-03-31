Checklist = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
             1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
             5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
             5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
             3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
set1 = set(Checklist)
MostBeen = list(set1)
Checklistrazn = []
print(f"Выдано чеков за неделю = {len(Checklist)}")
print(f"{len(set1)} разных людей посетило ресторан")
for i in MostBeen: #формировка списка из числа посещений разными людьми
    Checklistrazn.append(Checklist.count(i))
for i in range(len(MostBeen)):
    if Checklistrazn[i]==max(Checklistrazn):
        print(f"Работник с кодом {MostBeen[i]} был максимальное число раз = {Checklistrazn[i]}")

