x = int(input("Введите целое цисло от 0 до 10 "))
if x>=0 and x<=10:
    if x>=0 and x<=3:
        print("от 0 до 3")
    elif x>3 and x<6:
        print("от 4 до 5")
    else:
        print("от 6 до 10")
else:
    print("Число не в заданном диапозоне")