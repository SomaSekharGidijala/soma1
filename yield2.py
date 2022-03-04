def f1():
    print('10k')
    n=1000
    yield n

    print('10k lines of result')
    yield 3

result=f1()
n=result.__next__()
print(n)



