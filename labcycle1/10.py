str1=str(input("enter the word"))
list1=list(str1)
print(list1)
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)