def foo(list1,list2):
    l = []
    i1 = 0
    i2 = 0
    len1 = len(list1)
    len2 = len(list2)
    while True:
        if i1 >= len1 and i2 >= len2:
            break
        elif i1 >= len1:
            l.append(list2[i2])
            i2 += 1
        elif i2 >= len2:
            l.append(list1[i1])
            i1 += 1
        else:
            if list1[i1] < list2[i2]:
                l.append(list1[i1])
                i1 += 1
            else:
                l.append(list2[i2])
                i2 += 1
        
    return l

print(foo([],[0]))
