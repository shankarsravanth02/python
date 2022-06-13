def andSum(arr, n):
    a=0
    for i in range(0, 32):
        countSetBits = 0
        for j in range(0, n) :
            if (arr[j]&(1<<i)):
                countSetBits=countSetBits+1
        subset=((1<<countSetBits)-1)
        subset = (subset * (1 << i))
        a = a + subset
    return a
arr=[]
size=int(input())
for i in range(size):
    t=int(input())
    arr.append(t)
print(andSum(arr,size))