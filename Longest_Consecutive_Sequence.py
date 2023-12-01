
def foo(nums):
    if nums:
        sorted_list = (list(set(nums)))
        sorted_list.sort()

        first_index = sorted_list[0]
        count = 1
        all_sequence_count_list = []

        for i in sorted_list[1:]:
            if first_index + 1 == i:
                count += 1
            else:
                all_sequence_count_list.append(count)
                count = 1

            first_index = i
        all_sequence_count_list.append(count)
        return max(all_sequence_count_list)
    else:
        return 0

print(foo([1,23,4,6,7,8,3,5,1,3,4,5,2,3]))