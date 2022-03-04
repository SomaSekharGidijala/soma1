marks=[350,250,450,355,400]

"""
def f(x):
    return x+5

updated_marks=map(f,marks)
print(list(updated_marks))
"""

updated_marks=map(lambda x:x+5,marks)
print(list(updated_marks))