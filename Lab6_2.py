mytuple1 = (1, 2, 3)
element1= 1
mytuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
element2 = 3
mytuple3 = (2, 4, 6, 6, 4, 2)
element3 = 9
def delelintuple (mytuple,element):
    if element in mytuple:
        mylist = list(mytuple)
        mylist.remove(element)
        return tuple(mylist)
    else:
        return tuple(mytuple)
changetuple1=delelintuple(mytuple1,element1)
print(changetuple1)
changetuple1=delelintuple(mytuple2,element2)
print(changetuple1)
changetuple1=delelintuple(mytuple3,element3)
print(changetuple1)
