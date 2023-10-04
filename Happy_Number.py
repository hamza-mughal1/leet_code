def foo(n):
    t = n
    dic = {}
    while True:
        s = 0
        for i in str(t):
            s += int(i)**2
         
        if s == 1:
            return True
        elif s in dic:
            return False
        
        dic[s] = s
        t = s

print(foo(1))