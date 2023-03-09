def parenthesis(s):
    while(len(s)!=0):
        s = s.replace("()","")
        s = s.replace("[]","")
        s = s.replace("{}","")
        s = s.replace("{","{")
        s = s.replace("(","(")
        s = s.replace("[","[")
    if len(s)==0:
        return True
    else: return not True
print(parenthesis("["))
            