def foo(s,t):   
    while True:
        if len(s) != len(t):
            return False
        if s == "":
            return True

        s0 = s[0]
        s = s.replace(s0,"")
        t =  t.replace(s0,"")

s = "aaaagram"
t = "nagaram"

print(foo(s,t))       


