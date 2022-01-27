a= int(input("enter the fist number"))
b= int(input("enter the second number"))
c=  int(input("enter the third number"))
if (a>=b) and (b>=c):
    print(a,"is greater")
elif (b>=a ) and (b>=c) :
    print(b,"is greater")
else :
    print(c,"is greater")