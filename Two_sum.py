def foo(nums,target):
    for pos,i in enumerate(nums):
            for pos2,j in enumerate(nums[pos+1:]):
                if i+j == target:
                    return [pos,pos2+pos+1]
                