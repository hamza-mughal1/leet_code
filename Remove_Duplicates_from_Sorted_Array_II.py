def foo(nums):
    dic = {}
    res = []
    for i in nums:
        if dic.get(str(i)) == None:
            res.append(i)
            dic[str(i)] = 1
        elif dic.get(str(i)) <2:
            res.append(i)
            dic[str(i)] += 1
    
    nums[:] = res
