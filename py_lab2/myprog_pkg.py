#!/usr/bin/python

from my_pkg.binaryconver import *
from my_pkg.union_inter import *
if __name__=='__main__':
    while 1:
        select=int(input("Select menu: 1) conversion 2) union/intersection 3)exit? "))
        if(select==1):
            number=int(input("input binary number : "),base=2)
            OCTf(number)
            DECf(number)
            HEXf(number)
        elif(select==2):
            list1=input("1st list: ")
            list2=input("2nd list: ")
            unionf(list1,list2)
            intersectionf(list1,list2,)
        elif(select==3):
            print("exit the program...")
            exit(1)
        else:
            print("wrong input")
            select=0
