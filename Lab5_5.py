#list_1 = [1, 1, 3, 3, 1]
#
#list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
i = 0
while i < len(list_1):
    cnt = list_1.count(list_1[i])
    if cnt > 1:
        list_1[i] = str(list_1[i]) * cnt
    i += 1
print(set(list_1))
i = 0
while i < len(list_2):
    cnt = list_2.count(list_2[i])
    if cnt > 1:
        list_2[i] = str(list_2[i]) * cnt
    i += 1
print(set(list_2))
i = 0
while i < len(list_3):
    cnt = list_3.count(list_3[i])
    if cnt > 1:
        list_3[i] = str(list_3[i]) * cnt
    i += 1
print(set(list_3))
