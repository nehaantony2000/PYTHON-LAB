n1 = int(input('n1='))
n2= int(input("n2="))
if n1 < n2 :
    small = n1
else :
    small = n2
for i in range (1,small+1):
          if ((n1%i == 0) and (n2%i == 0) ):
              hcf = i

print ("hcf",hcf)