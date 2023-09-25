def rotate(nums, k) :
        k = k % len(nums)
        
        n = 0
        n = len(nums) - k
        head = nums[n:]

        nums[n:],nums[:n] = nums[:n],nums[n:]

        return nums