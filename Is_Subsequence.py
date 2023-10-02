def foo(s,t):
    n = 0
    l = len(s)
    for i in t:
        if n == l:
            return True
        if i == s[n]:
            n += 1
    if n == l:
        return True
    return False


s = "b"
t = "abc"

print(foo(s,t))