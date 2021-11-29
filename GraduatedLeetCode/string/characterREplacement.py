from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    ## RC ##
    ## APPROACH : SLIDING WINDOW ##
    # Logic #
    # 1. Increase the window if the substring is valid else,
    # 2. slide the window with the same length. No need to shrink the window

    ## TIME COMPLEXITY : O(N) ##
    ## SPACE COMPLEXITY : O(N) ##

    freqDict = defaultdict(int)
    maxFreq = 0
    maxLength = 0
    start = end = 0

    while end < len(s):
        last_char = s[end]
        freqDict[last_char] += 1

        # maxFreq may be invalid at some points, but this doesn't matter
        # maxFreq will only store the maxFreq reached till now

        maxFreq = max(maxFreq, freqDict[last_char])

        # maintain the substring length and slide the window if the substring is invalid
        sub_string_length = (end - start + 1)
        non_repeating_chars = sub_string_length - maxFreq
        if (non_repeating_chars) > k:
            first_char = s[start]
            freqDict[first_char] -= 1
            start += 1
        else:
            maxLength = max(maxLength, sub_string_length)
        end += 1
    return maxLength

print(characterReplacement("GGUIVILPZJXWWZLVKETZWWFKDYCRQICLYYJDMRCQVCSFCSKRMKCFUNAECJVRLAIWFJADSNNYDPXVYGPNCL", 2))
# For example, string = GGUIVIL and k = 2
#variable start denotes the beginning of the sliding window, the key will be start, the value will be the letter.
#If the curr value (start + whatever)
#
#
#