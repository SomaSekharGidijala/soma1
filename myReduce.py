from functools import reduce

marks=[88,65,77,93,99]

def f(x,y):
    return x+y

totalMarks=reduce(f,marks)
print(totalMarks)