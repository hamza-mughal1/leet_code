def binary_search(nums,target):
    left = 0
    right = len(nums)

    while True:
        pos = (left+right)//2
        if nums[pos] == target:
            return pos
        
        elif left == right-1:
            if target < nums[0]:
                return 0
            return pos + 1
        
        elif nums[pos] > target:
            right = pos

        elif nums[pos] < target:
            left = pos

        


print(binary_search([1,3,5,6],1))
