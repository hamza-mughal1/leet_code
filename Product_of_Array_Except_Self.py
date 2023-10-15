def foo(nums):
    n = 1
    l = []
    for i in nums:
        n*= i
    for i in nums:
        if i == 0:
            l.append(0)
        else:
            l.append(n//i)
    return l


print(foo([-1,1,0,-3,3]))