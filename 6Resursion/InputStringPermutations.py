def generate_permutations(word, input_list, set):
    if len(input_list) == 1:
        old_word = word
        word = word + input_list[0]
        if word in set:
            print(True)
        set.add(word)
        return

    i = 0
    while i < len(input_list):
        if i == 0:
            new_input_list = input_list[1:]
        elif i == len(input_list)-1:
            new_input_list = input_list[:i]
        else:
            new_input_list = input_list[:i] + input_list[i+1:]
        new_word = word + input_list[i]
        generate_permutations(new_word, new_input_list, set)
        i+=1


    return

input = "history"
permutationSet = set()

generate_permutations("", list(input), permutationSet)

print(permutationSet)