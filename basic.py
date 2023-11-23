def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

op='''
1.add
2.sub
3.mul
4.div
5.exit
'''

ch=int(input("Enter Your Choice:"))

a=int(input("Enter a Value:"))
b=int(input("Enter b Value:"))
print(f"The Addition Value Of a and b is : {add(a,b)}")