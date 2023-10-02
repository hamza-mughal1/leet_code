def foo(s):
    t = "abcdefghijklmnopqrstuvwxyz1234567890"
    s = s.lower()
    r = len(s)
    i = 0
    while True:
        if i >= len(s):
            break
        if s[i] not in t:
            s = s.replace(s[i],"")
        else:
            i +=1
    return s == s[::-1]

print(foo("A man, a plan, a canal: Panama")) 
