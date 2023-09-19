import math
import time
l = [1,8,6,2,5,4,8,3,7]





def foo(l):
    area = 0
    for pos1,i in enumerate(l):
        x1 = pos1
        x2 = x1
        for j in l[x1:]:
            minimum = min(i,j)
            absolute = abs(x1-x2)
            num = minimum*absolute
            area = max(num,area)
            x2 +=1
    return area


def poo(l):
    area = 0
    i = (0,l[0])
    j = (len(l)-1,l[-1])
    while True:
        minimum = min(i[1],j[1])
        absolute = abs(i[0]-j[0])
        num = minimum*absolute
        area = max(num,area)
        if i[1] == min(i[1],j[1]):
            n = 1
            while True:
                if (l[i[0]+n] > i[1]) and (i[0]+n < j[0]):
                    i = (i[0]+n,l[i[0]+n])
                    break
                else:
                    if i[0]+n >= j[0]:
                        return area
                n+=1

        elif j[1] == min(i[1],j[1]):
            n = 1
            while True:
                if (l[j[0]-n] > j[1]) and (j[0]-n > i[0]):
                    j = (j[0]-n,l[j[0]-n])
                    break
                else:
                    if j[0]-n <= i[0]:
                        return area
                n+=1

start = time.time()
foo(l)
end = time.time()
start2 = time.time()
poo(l)
end2 = time.time()

print("time 1 : ",end-start)
print("time 2 : ",end2-start2)

