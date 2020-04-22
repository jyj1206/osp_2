#!/usr/bin/python

def unionf(a,b):
    arr1=[]
    arr2=[]
    a=a.replace('[','')
    a=a.replace(']','')
    a=a.replace(' ','')
    for num in a.split(','):
        arr1.append(int(num))
    b=b.replace('[','')
    b=b.replace(']','')
    b=b.replace(' ','')
    for num2 in b.split(','):
        arr2.append(int(num2))
    arr3=list(set(arr1).union(set(arr2)))
    print("=> union ",end="")
    print(arr3)
def intersectionf(a,b):
    arr1=[]
    arr2=[]
    a=a.replace('[','')
    a=a.replace(']','')
    a=a.replace(' ','')
    for num in a.split(','):
        arr1.append(int(num))
    b=b.replace('[','')
    b=b.replace(']','')
    b=b.replace(' ','')
    for num2 in b.split(','):
        arr2.append(int(num2))
    arr3=list(set(arr1).intersection(set(arr2)))
    print("=> intersection ",end="")
    print(arr3)

if __name__=='__main__':
    print("this is my_module...")
