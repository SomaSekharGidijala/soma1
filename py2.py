from sys import getsizeof

r=range(1,10)

def f1():
    return(list(r))

def f2():
    yield list(r)

cf1 = f1()
print ('result',getsizeof(cf1))

cf2 = f2()
print(cf2)
print ('reselt1',getsizeof(cf2))