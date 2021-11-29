def minSteps( s, t):
    charArray = [0] * 26

    for char in s:
        charArray[ord(char) - ord('a')] += 1

    # print(charArray)

    for char in t:
        charArray[ord(char) - ord('a')] -= 1

    count = 0
    # print(charArray)
    for val in charArray:
        if val > 0:
            print (val)
            count += val

    return count

print(minSteps("abcdef", "hijklmn"))