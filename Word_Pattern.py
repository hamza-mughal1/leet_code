def foo(pattern,s):
    pat = s.split(" ")
    if len(pattern) != len(pat):
        return False
    dic1 = {}
    dic2 = {}
    for pos,i in enumerate(pat):
        if i in dic1:
            if pattern[pos] != dic1[i]:
                return False
        else:
            dic1[i] = pattern[pos]
        
        if pattern[pos] in dic2:
            if i != dic2[pattern[pos]]:
                return False
        else:
            dic2[pattern[pos]] = i
    return True


print(foo("abbba","dog cat cat dog"))