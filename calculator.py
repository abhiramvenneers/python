print("Enter your choice")
print("\n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXIT\n")
n=int(input())
if n>0 and n<=5:    
    if n==1:
        print("Enter two numbers: ")
        a=int(input())
        b=int(input())
        add=a+b
        print("{0}+{1}={2}".format(a,b,add))
    elif n==2:
        print("Enter two numbers: ")
        a=int(input())
        b=int(input())
        sub=a-b
        print("{0}-{1}={2}".format(a,b,sub))    
    elif n==3:
        print("Enter two numbers: ")
        a=int(input())
        b=int(input())
        mult=a*b
        print("{0}*{1}={2}".format(a,b,mult))  
    elif n==4:
        print("Enter two numbers: ")
        a=int(input())
        b=int(input())
        div=a/b
        print("{0}/{1}={2}".format(a,b,div)) 
    elif n==5:
        print("\n\nPROGRAM EXITED\n THANKYOU")
else:
    print("WRONG CHOICE!")
