input = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
starting_pos = 28

def find_closing_pos(input, start):

    counter = 1
    pos = start + 1

    for char in list(input)[start+1:]:

        if char == "(":
            counter += 1
        if char == ")":
            counter -=1
        if counter == 0:
            return pos
        pos+=1


print(find_closing_pos(input, starting_pos))