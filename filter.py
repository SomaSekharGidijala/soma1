marks=[350,250,450,355,400]
"""
def f(x):
    return x>350

filterd_marks=filter(f,marks)
print(list(filterd_marks))
"""

filterd_marks=filter(lambda x:x>350,marks)
print(list(filterd_marks))