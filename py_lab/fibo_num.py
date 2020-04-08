#!/usr/bin/python
n=int(input("fibonacci number? "))
count=1
while count!=n+1:
    if(count==1)or(count==2):
        a=1
        b=1
        print("%d" %b,end=',')
    else:
        c=b
        b=a+b
        a=c
        if(count==n):
            print("%d" %b)
        else:
            print("%d" %b,end=',')
    count+=1
print("F%d = %d" %(n,b))
