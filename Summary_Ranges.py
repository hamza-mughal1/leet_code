def foo(nums):
    l = len(nums)
    if l==0:
        return []
    elif l == 1:
        return [str(nums[0])]
    n = []
    start = 0
    pre = nums[0]
    state = False
    for pos,i in enumerate(nums[1:]):
        if pre+1 != i:
            if nums[start] == pre:
                n.append(str(pre))
            else:
                n.append(f"{nums[start]}->{pre}")
            start = pos+1
            state = False
        else:
            state = True
            
            
        pre = i

    if state:
        n.append(f"{nums[start]}->{pre}")
    else:
        n.append(str(pre))
    return n


print(foo([0,1,2,4,5,7]))
        