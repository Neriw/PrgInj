tuple1=(1, 2, 3)
tuple2=(1, 8, 3, 4, 8, 8, 9, 2)
tuple3=(1, 2, 8, 5, 1, 2, 9)
id1=8
def validate(tuple, id):
    if tuple.count(id)>0:
        s_id=tuple.index(id)
        e_id=tuple.index(id,s_id+1) if tuple.count(id)>1 else ()
        return tuple[s_id:e_id+1] if e_id !=() else tuple[s_id:]
    else:
        return ()
print(validate(tuple1,id1))
print(validate(tuple2,id1))
print(validate(tuple3,id1))