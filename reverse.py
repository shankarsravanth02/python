# def reve(s):
#     return s[::-1]
# print(reve("krishna"))

# def reve(s):
#     return reve(s[::-1])+s[0]
# print(reve("krishna"))

# def work1(f1,s1):
#     return f1*s1
# def work2(f2,s2):
#     return f2*s2

# def work():
#     f1=int(input("enter F1: ")) 
#     s1=int(input("enter s1: "))
#     f2=int(input("enter f2: "))
#     s2=int(input("enter s2: "))   
#     if((f1 or s1 or f2 or s2)<0):
#         return "error"
#     else:
#         return max(work1(f1,s1),work2(f2,s2)),work1(f1,s1)+work2(f2,s2)
# print(work())

# def flip(state,n):
#     if(state=="H" and n%2==0):
#         return "H"
#     elif(state=="H" and n%2!=0):
#         return "T"
#     elif(state=="T" and n%2==0):
#         return "T"
#     else:
#         return "H"
# print(flip("H",5))


