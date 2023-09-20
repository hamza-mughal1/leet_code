
nums = [0,1,2,2,3,0,4,2]
val = 2

def foo(nums,val):
    nums[:] = [i for i in nums if i!=val]