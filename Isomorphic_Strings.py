def foo(s,t):
    dic1 = {}
    dic2 = {}
    for pos,i in enumerate(s):
        if i in dic1:
            if t[pos] != dic1[i]:
                return False
        else:
            dic1[i] = t[pos]
        
        if t[pos] in dic2:
            if i != dic2[t[pos]]:
                return False
        else:
            dic2[t[pos]] = i
    return True

print(foo("badc","baba"))