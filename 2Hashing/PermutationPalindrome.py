def permutationOfPalindrome(string):

    char_dict = {}

    for char in string:
        if(char_dict.get(char) == None):
            char_dict[char] = 1
        else:
            char_dict[char] = char_dict[char] + 1
    # print(char_dict)

    odd_count = 0
    for item in char_dict:
       if (char_dict[item] % 2 !=0):
           odd_count = odd_count + 1

    if(odd_count > 1):
        return False
    return True


print(permutationOfPalindrome("civci"))