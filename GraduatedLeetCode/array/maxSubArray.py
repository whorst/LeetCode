def maxSubArray(nums) -> int:
    largest = nums[0]
    continuous = nums[0]

    for num in nums[1:]:
        new_cont = continuous + num
        if num > new_cont:
            continuous = num
            if continuous > largest:
                largest = continuous
            continue
        if new_cont > largest:
            largest = new_cont
        continuous = new_cont

    return largest

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))