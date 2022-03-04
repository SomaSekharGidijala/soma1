from sys import getsizeof

def f1():
    return list(range(1,101))

def f2():
    yield list(range(1,101))

result1=f1()
print(result1)
print('size', getsizeof(result1))
result2=f2()
print(list(result2))
print('size', getsizeof(result2))