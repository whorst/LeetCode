def threeSum(self, nums):
    ret = []
    s = sorted(nums)
    for index, num in enumerate(s):
        i = index + 1
        j = len(s) - 1
        if index > 0 and num == s[index - 1]:
            continue
        while i < j:
            if (j < len(s) - 1 and s[j] == s[j + 1]):
                j -= 1
                continue
            if num + s[i] + s[j] == 0:
                ret.append([num, s[i], s[j]])
                i += 1
                j -= 1
                # ret.append()
            if (num + s[i] + s[j] < 0):
                i += 1
            elif (num + s[i] + s[j] > 0):
                j -= 1
    print(ret)
    return ret

# Find the sum of three numbers in a list that equal to 0
# Time complexity is O(N)^2
# Space is O(N)