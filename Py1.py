f1=[10,11,12,13,14,12]
count=0
c=[]
no = int(input('Enter Value'))
for val in f1:
    if(no==val):
        c=[val]
        count=count+1
        print(count)
    for a in c:
        print('Hi')  
else:
    print('Not Found')
