def rotate(self, nums, k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        n = 0
        n = len(nums) - k
        head = nums[n:]

        nums[n:],nums[:n] = nums[:n],nums[n:]

        return nums