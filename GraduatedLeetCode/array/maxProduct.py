def maxProduct(nums) -> int:
    totalmax, maximum, minimum = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        temp = maximum
        #            new_num       new_num*max         new_num*min
        maximum = max(nums[i], nums[i] * maximum, nums[i] * minimum)
        minimum = min(nums[i], nums[i] * temp, nums[i] * minimum)
        print(minimum)
        totalmax = max(totalmax, maximum)
    return totalmax

maxProduct([-2,3,-4])