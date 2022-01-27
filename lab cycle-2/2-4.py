li1=[2,3,4,5,6,7]
li2=[5,6,7,8,10,12]
if len(li1)==len(li2):
    print("a-Length are same\n")
else:
    print("a-lenth are not same")
if sum(li1) == sum(li2):
    print("b-sum are equal")
else:
    print("b-sum are not equal")
j=[x for x in li1 if x in li2]
if j != 0:
    print("c-same elements are",str(j))
else:
    print("c-no elements found")