def pawri():
    n=int(input())
    l1=[]
    for i in range(n):
        s=input()
        s1=""
        if(s.rfind("party")==1 or s.rfind("party")!=1):
            s1=s.replace("party","pawri")
            l1.append(s1)
    for j in l1:
        return j
print(pawri())