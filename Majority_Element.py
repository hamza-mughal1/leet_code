def foo(nums):
    l = len(nums)
    if l<2:
        return nums[0]
    nums.sort()
    if l%2 == 0:
        return nums[int(l/2)]
    return nums[int((l/2)-0.5)]
