small=int(input("enter small number:"))
big=int(input("enter big number:"))
for i in range(small,big+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else: print(i)