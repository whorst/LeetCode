def productExceptSelf(nums):
    n = len(nums)
    res = []
    dp_l = [1] * n
    dp_r = [1] * n

    for i in range(1, n):
        dp_l[i] = dp_l[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        dp_r[i] = dp_r[i + 1] * nums[i + 1]

    for i in range(n):
        res.append(dp_l[i] * dp_r[i])
    return res


def productExceptSelf(nums):
    # Create an array that will return
    ret = [1] * len(nums)
    # Store the cumulative product
    cumprod = 1

    # Iterate over nums
    for i in range(len(nums)):
        ret[i] = cumprod
        cumprod = nums[i] * cumprod

    cumprod = 1

    for i in range(len(nums) - 1, -1, -1):
        ret[i] *= cumprod
        cumprod = nums[i] * cumprod

    return ret


def productExceptSelf(nums):
    ret_arr = [1] * len(nums)
    computation = 1

    for i in range (0, len(nums)):
        ret_arr[i] = computation
        computation = ret_arr[i] * nums[i]

    computation = 1
    for i in range(len(nums)-1, -1, -1):
        ret_arr[i] = computation
        computation = computation * nums[i]

    print(ret_arr)

def productOfArrayExceptSelf(nums):
    ret_arr = [1] * len(nums)
    left_iter = nums[0]
    ret_arr[0] = 1

    for i in range(1, len(nums)):
        ret_arr[i] *= left_iter
        left_iter *= nums[i]

    print(ret_arr)
    right_iter = nums[len(nums) -1]
    print(right_iter)
    for j in range(len(nums) -2, -1, -1):
        ret_arr[j] *= right_iter
        right_iter *= nums[j]

    print(ret_arr)



print(productOfArrayExceptSelf([2,3,4]))
