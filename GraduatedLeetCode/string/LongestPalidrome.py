def longestPalindrome(s: str) -> str:
    res = ""
    size = 0
    center = 0
    n = len(s)
    while center < n:
        left = center - 1
        right = center + 1
        while right < n and s[right] == s[center]:
            # While right does not touch the end and right is equal to center
            right += 1
        while left >= 0 and right < n and s[left] == s[right]:
            # Iterate forwards and backwards at the same time
            left -= 1
            right += 1
        if right - left - 1 > size:
            # If the found palindrome is greater than the biggest found palindrome
            size = right - left - 1
            res = s[left + 1:right]
        center += 1
    return res

print(longestPalindrome("abccdefgh"))