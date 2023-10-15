def foo(nums):
    r = []
    l = []
    r1 = 1
    l1 = 1
    final = []
    for i in range(len(nums)):
        l_product = l1*nums[i]
        r_product = r1*nums[-(i+1)]
        
        l.append(l_product)
        r.append(r_product)

        l1 = l_product
        r1 = r_product

    r.reverse()

    for j in range(len(nums)):
        if j == 0:
            final.append(r[1])
            continue
        elif j == len(nums)-1:
            final.append(l[-2])
            continue

        l2 = l[j-1]
        r2 = r[j+1]
        final.append(l2*r2)

    return final


print(foo([-1,1,0,-3,3]))