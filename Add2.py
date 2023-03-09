def addtwo(l1,l2):
    s1,s2="",""
    for i in reversed(l1):
        s1=s1+str(i)
    for j in reversed(l2):
        s2=s2+str(j)
    l=int(s1)+int(s2)
    res=map(int,str(l))
    res1=list(res)
    return [k for k in reversed(res1)]
n1=int(input("enter number of elements in l1: "))
r1=[input(i) for i in range(n1)]
n2=int(input("enter number of elements in l2: "))
r2=[input(j) for j in range(n2)]
print(addtwo(r1,r2))