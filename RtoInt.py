def RtoInt(s):
    sum=0
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(s),1):
        # if i=='I' and i+1=="V":
        #     d[i]=4
        # elif i=='I' and i+1=="X":
        #     d[i]=9
        # elif i=='X' and i+1=="L" :
        #     d[i]=40
        # elif i=='X' and i+1=="C" :
        #     d[i]=90
        # elif i=='C' and i+1=="D":
        #     d[i]=400
        # elif i=='C' and i+1=="M":
        #     d[i]=900
        sum=sum+d[i]
    return sum
print(RtoInt("XIV"))