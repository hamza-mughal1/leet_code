def doo(s,t):   
    while True:
        if len(s) != len(t):
            return False
        if s == "":
            return True

        s0 = s[0]
        s = s.replace(s0,"")
        t =  t.replace(s0,"")


def foo(strs):
    if len(strs) == 1:
        return [[strs[0]]]
    l = []
    l.append([strs[0]])
    switch = True
    for i in strs[1:]:
        for j in range(len(l)):
            if doo(l[j][0],i):
                l[j].append(i)
                switch = False
                break

        if switch:
            l.append([i])
        switch = True
    return l

print(foo(["a"]))
