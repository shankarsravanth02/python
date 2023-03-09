def strstr(h,n):
    # if h=="" and n=="":
    #     return 0
    # elif n in h:
    #     return h.find(n)
    # else: return -1
    for i in h:
        for j in n:
            if i==j:
                i=i+1
                j=j+1
                return i
        else: i=i+1
print(strstr("hello","ll"))
