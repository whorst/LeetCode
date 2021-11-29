def findMin(nums) -> int:
    min_pointer = 0
    max_pointer = len(nums) - 1
    mid_pointer = min_pointer + max_pointer // 2

    while (True):
        if ((min_pointer + 3) >= max_pointer):
            min_num = nums[min_pointer]
            for i in range(min_pointer, max_pointer + 1):
                if min_num > nums[i]:
                    min_num = nums[i]
            return min_num
        min_num = nums[min_pointer]
        mid_num = nums[mid_pointer]
        max_num = nums[max_pointer]

        if mid_num > max_num:
            min_pointer = mid_pointer
            max_pointer = max_pointer
            mid_pointer = ((max_pointer - min_pointer) // 2) + min_pointer
        else:
            min_pointer = min_pointer
            max_pointer = mid_pointer
            mid_pointer = ((max_pointer - min_pointer) // 2) + min_pointer

print(findMin([4,5,6,7,8,9,1,2,3]))