def numRecursive(num_str, index, terminal):
    #https://leetcode.com/problems/decode-ways/discuss/1029225/Simple-and-detail-solution-with-explanation
    if (index >= len(num_str)):
        terminal[0] = terminal[0] + 1
        return

    first_one = int(num_str[index])
    if num_str[index] == "0":
        return

    if (index + 1 >= len(num_str)):
        terminal[0] = terminal[0] + 1
        return

    first_two = int(num_str[index] + num_str[index + 1])

    if first_two > 26:
        first_two = None

    numRecursive(num_str, index + 1, terminal)

    if first_two != None:
        numRecursive(num_str, index + 2, terminal)


def numDecodings(s):
    if s[0] == "0":
        return 0

    if len(s) == 1:
        return 1

    terminal = [0]
    first_one = int(s[0])
    first_two = int(s[0] + s[1])

    if len(s) == 2 and first_two <= 26:
        if first_two == 10 or first_two == 20:
            return 1
        return 2

    numRecursive(s, 1, terminal)
    if (first_two <= 26):
        numRecursive(s, 2, terminal)

    return terminal[0]

print(numDecodings("1234"))