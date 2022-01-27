list1 = [1, 9, 10, 11, -56, 12, 0, 78, -77, 789, -34, 67]
for i in list1:
       if i <= 0:
            list1.remove(i)
print(list1)
list2=[1,2,90,87,100,102,6,1,4]
for i in list1:
    print (i*i)
word=input("enter the word")
j=[ord(x) for x in word]
print(j)
V=['a','e','i','o','u']
s=[i for i in word if i in V]
print(s)