def foo(digits):
    if digits:
        carry = 1
        l = []
        for i in digits[::-1]:
            n = i + carry
            if n >= 10:
                l.append(n%10)
                carry = 1
            elif n < 10:
                l.append(n)
                carry = 0
        
        if carry:
            l.append(carry)
        
        return l[::-1]
    return []
print(foo([]))
