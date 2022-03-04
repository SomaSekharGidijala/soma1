def f1():
    print('1')
    yield 1
    print('2')
    yield 2
    print('3')
    yield 3

result=f1()
result.__next__()
result.__next__()
result.__next__()