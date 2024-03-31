from math import sqrt
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
StoronaMax = []
Storonamin = []
four = one+three+two
for i in range(3):
    StoronaMax.append(max(four))
    Storonamin.append(min(four))
    four.pop(four.index(max(four)))
    four.pop(four.index(min(four)))
pmax = (StoronaMax[0] + StoronaMax[1] + StoronaMax[2]) / 2
MaxSquare = sqrt(pmax * (pmax - StoronaMax[0]) * (pmax - StoronaMax[1]) * (pmax - StoronaMax[2]))
pmin= (Storonamin[0] + Storonamin[1] + Storonamin[2]) / 2
MinSquare = sqrt(pmin * (pmin - Storonamin[0]) * (pmin - Storonamin[1]) * (pmin - Storonamin[2]))
print(f"площади треугольника из максимальных элементов = {MaxSquare}")
print(f"площади треугольника из минимальных элементов = {MinSquare}")