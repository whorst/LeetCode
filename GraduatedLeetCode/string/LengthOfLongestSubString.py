def lengthOfLongestSubstring(s: str) -> int:
    #longest non repeating substring
    str_len = len(s)
    if str_len == 0:
        return 0

    longest = s[0]

    center = 0

    while (center < str_len):
        char_set = set()
        char_set.add(s[center])
        left = center - 1
        right = center + 1

        while right < str_len and ((s[right] in char_set) == False):
            char_set.add(s[right])
            right += 1
        if (len(s[center:right])) > len(longest):
            longest = s[center:right]

        while left >= 0 and s[left] in char_set == False:
            char_set.add(s[left])
            left -= 1

        if (len(s[(left + 1):right])) > len(longest):
            longest = s[(left + 1):right]
        center += 1

        print(s[left + 1:right])

    return len(longest)

print(lengthOfLongestSubstring("abccccdefgh"))
