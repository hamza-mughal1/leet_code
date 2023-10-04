def foo(nums,k):
    dic1 = {}
    n = 10**5
    for pos,i in enumerate(nums):
        if i in dic1:
            n = min(n,abs(dic1[i]-pos))
        dic1[i] = pos

    if n <= k:
        return True
    return False


n = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
k = 1
print(foo(n,k))