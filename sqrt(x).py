def foo(x):
    l, r = 0, x // 2 if x > 1 else x
    while l <= r:
        mid = (l + r) // 2
        mid2 = mid * mid

        if mid2 == x:
            return mid
        elif mid2 < x:
            l = mid + 1
        elif mid2 > x:
            r = mid - 1
    
    return r

print(foo(8))