def lengthOfLIS(nums) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    # The trick here is pretty bad. Init the DP cache, every element to 1. Dp[i] is supposed to represent the amount of numbers
    # that are of lesser value that have appeared before that number. From there, check if dp[i] > dp[j] + 1. If dp[j] +1 is
    # bigger, that we set dp[i] to dp[j] + 1

    for i in range(1, n):
        for j in range(i):
            focus = nums[i]
            current = nums[j]
            if focus > current:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))