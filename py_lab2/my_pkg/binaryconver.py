#!/usr/bin/python
def OCTf(value):
    o=oct(value)
    print("=> OCT> ",end="")
    o=o.replace('0o','')
    print(o)

def DECf(value):
    s=str(value)
    print("=> DEC> ",end="")
    print(s)

def HEXf(value):
    h=hex(value)
    print("=> HEX> ",end="")
    h=h.replace('0x','')
    print(h.upper())

if __name__=='__main__':
    print("this is my_module...")



