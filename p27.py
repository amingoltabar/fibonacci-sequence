n=int(input('enter the number of sequences you want to be shown '))
a=0
b=1
print(b)
for i in range(1,n,1):
    c=a+b
    print(c)
    a=b
    b=c
