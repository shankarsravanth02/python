def primed(y):
    for j in range(2,y):
        if(y%j==0):
            return False
    return True
def twinPrimes(min,max):
    for i in range(min,max+1):
        k=i+2
        if(primed(i) and primed(k)):
            print("(",i,",",k,")")
twinPrimes(4,100)