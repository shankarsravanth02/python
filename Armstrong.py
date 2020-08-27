n=int(input("enter number:"))
n1=n
sum1=0
sum2=0
while(n>0):
    digit=n%10
    sum1=sum1+digit
    temp=digit*digit*digit
    sum2=sum2+temp
    n=n//10
print(sum1,"is sum of digits of number",n)
if(n1==sum2):
    print(n1,"is armstrong number")
else: print(n1,"is not armstrong number")
