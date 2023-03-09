def lswr(s):
    temp=[]
    for i in s:
        if i not in temp:
            temp.append(i)
    return len(temp)
print(lswr("pwwkew"))