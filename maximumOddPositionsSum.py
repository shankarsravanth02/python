def maximumOddPositionsSum(n:int,arr: list[int]):
    maxx=arr[0]
    sum=0
    l=[]
    if(n%2==0):
        for i in range((n//2)):
            if(maxx<arr[i]):
                arr[i]=maxx
                l.append(arr[i])
            else: l.append(maxx)
    if(n%2!=0):
        for i in range((n//2)+1):
            if(maxx<arr[i]):
                arr[i]=maxx
                l.append(arr[i])
            else: l.append(maxx)
    for i in l:
        sum+=i
    print(sum)
maximumOddPositionsSum(8,[1,7,3,4,7,6,2,9])