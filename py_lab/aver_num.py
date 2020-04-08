#!/usr/bin/python
N=int(input("How many input number?: "))
count=N
sumnum=0
while count>0:
    num=int(input("input your number: "))
    sumnum+=num
    count-=1
average=sumnum/N
print("output average: %f" %average)

