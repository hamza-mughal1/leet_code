strs = ["a"]


def foo(strs):
    if len(strs) == 1:
        return strs[0]
    
    if len(strs[0]) ==0:
        return ""
    
    pre = strs[0]
    for i in strs[1:]:
        if i == "":
            return ""
        word = ""
        for j in range(len(min(pre,i))):
            if pre[j] == i[j]:
                word += pre[j]
            else:
                break

        pre = word 

    return pre
        

print(foo(strs))
    
    
