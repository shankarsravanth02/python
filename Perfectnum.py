k=int(input("enter to check:"))
sum=0
for i in range(1,k):
    if(k%i==0):
        sum=sum+i
if(sum==k):
    print(k,"is perfect number")
else: print(k,"is not a perfet number")