nums1 = []
nums2= [1]
m = 0
n = 1



def foo(nums1,m,nums2,n):
    l = []
    a,b = 0,0
    while True:
        x = None
        y = None
        if m>=1:
            x = nums1[a]
        if n>=1:
            y = nums2[b]
        if (x != None):
            try:
                if (x == min(x,y)):
                    l.append(x)
                    a+=1
                    m-=1
            except:
                l.append(x)
                a+=1
                m-=1
        if (y != None):
            try:
                if (y == min(x,y)):
                    l.append(y)
                    b+=1
                    n-=1
            except:
                l.append(y)
                b+=1
                n-=1
        if m<1 and n<1:
            nums1[:] = l
            break
        


    

foo(nums1,m,nums2,n)

print(nums1)

