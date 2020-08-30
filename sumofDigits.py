r=int(input("enter number:"))
sum=0
while (r>0):
    rem=r%10
    sum=sum+rem
    r=r//10
print(sum)