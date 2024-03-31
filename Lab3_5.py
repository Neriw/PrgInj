string="hellow"
counter=0
values =[0,2,4,6,8,10]
while counter!=10:
    memory=string
    if counter in values:
        string=string+" world"
    print(string)
    if counter<10:
        string=memory
    counter+=1
while " world" not in string:
    memory=" world"
    print(string+memory)
    if counter>7:
        string=" world"