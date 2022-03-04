elements=[12,3,34,333,45]

no=int(input("Enter no"))

for i in elements:
    if(no == i):
        print('existed')
else:
    print('not existed')