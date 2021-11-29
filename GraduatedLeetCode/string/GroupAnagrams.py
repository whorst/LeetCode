def groupAnagrams(strs):
    anag_dict = {}
    for word in strs:
        sorted_word = str(sorted(word))
        if anag_dict.get(sorted_word) == None:
            anag_dict[sorted_word] = []
        anag_dict[sorted_word].append(word)
    print(anag_dict)

    ret_list = []
    for key in anag_dict.keys():
        ret_list.append(anag_dict.get(key))
    return ret_list