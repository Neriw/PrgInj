import random


def kubik():
    x=random.randint(1,6)
    print(f"На кубике выпало = {x}")
    if x==5 or x==6:
        print("Вы победили")
    elif x==3 or x==4:
        kubik()
    else:
        print("Вы проиграли")


if __name__ == '__main__':
    kubik()