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
  
while True:
    print(op)
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        a=int(input("Enter a Value:"))
        b=int(input("Enter b Value:"))
        print(f"The Addition Value Of a and b is : {add(a,b)}") 
    elif ch==2:
        a=int(input("Enter a Value:"))
        b=int(input("Enter b Value:"))
        print(f"The Subtraction Value Of a and b is : {sub(a,b)}")
    elif ch==3:
        a=int(input("Enter a Value:"))
        b=int(input("Enter b Value:"))
        print(f"The Multiplication Value Of a and b is : {mul(a,b)}")
    elif ch==4:
        a=int(input("Enter a Value:"))
        b=int(input("Enter b Value:"))
        print(f"The Division Value Of a and b is : {div(a,b)}")
    elif ch==5:
        exit()
    else:
        print("Something Went Wrong! Try Again")
