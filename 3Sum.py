def twoSum(numbers : list[int], target : int) -> list:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        R = 0
        L = len(numbers)-1
        while True:
            condition = numbers[R] + numbers[L]
            if (condition) == target:
                return [numbers[R],numbers[L]]
            if R == L:
                return None
            if (condition) > target:
                L -= 1
            if (condition) < target:
                R += 1


def threeSum(nums : list):
    sorted_list = list(set(sorted(nums)))
    final_list = []

    for pos,i in enumerate(sorted_list):
        l = twoSum(sorted_list[pos:],-i)
        if l:
             final_list.append([i,l[0],l[1]])
    
    return final_list


print(threeSum([-1,0,1,2,-1,-4]))