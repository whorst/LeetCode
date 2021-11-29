list_with_duplicate = [3, 4, 2, 3, 1, 5]
list_with_duplicate = [4, 3, 1, 1, 4]
list_with_duplicate = [2, 4, 1, 3, 7, 3, 5, 6]
# list_with_duplicate = [4,3,1,1,4]


def find_duplicate(duplicate_list):
    trailing_head = None

    head_index = len(duplicate_list) -1
    head_pointer = duplicate_list[-1]

    cycle_index = head_index
    cycle_pointer = head_pointer

    i = 0
    while i < len(duplicate_list) - 1:
        cycle_pointer = duplicate_list[cycle_pointer - 1]
        i += 1

    while cycle_pointer != head_pointer:
        i = 0
        while i < len(duplicate_list) - 1:
            cycle_index = cycle_pointer -1
            cycle_pointer = duplicate_list[cycle_pointer - 1]
            if (cycle_pointer == head_pointer):
                if(head_index != cycle_index):
                    return head_pointer
                if trailing_head == None:
                    return head_pointer
                else:
                    return trailing_head
            i += 1
        trailing_head = head_pointer

        head_index = head_pointer -1
        head_pointer = duplicate_list[head_pointer - 1]


print(find_duplicate(list_with_duplicate))
