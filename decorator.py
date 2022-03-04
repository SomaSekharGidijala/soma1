
def m1(a):
    def m2():
        x=a() #a=m3
        return x+100
    return m2

@m1
def m3():
   return 100

result=m3
print(result())

#result=m1(m3)
#output=result()
#print(output)