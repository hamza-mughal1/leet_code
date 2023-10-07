def foo(s):
    if len(s) == 1:
        return False
    l = []
    for i in s:
        if (i == "(") or (i == "[") or (i == "{"):
            l.append(i)
            continue
        n = l.pop()
        if i == ")" and n != "(":
            return False
        elif i == "]" and n != "[":
            return False
        elif i == "}" and n != "{":
            return False
        
    
    if len(l)>0:
        return False
    return True


print(foo("([{}])"))