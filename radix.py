def calcLength(n:int,m:int,k:int)->int:
        s=""
        l1=[]
        for i in range(m):
            for j in str(n):
               n1=int(j)
               n1+=k
               s+=str(n1)
            n=s
            l1.append(len(s))
            s=""
        print(l1[-1])
n=int(input())
for i in range(n):
    x=int(input())
    y=int(input())
    z=int(input())
for j in range(n):
    calcLength(x,y,z)