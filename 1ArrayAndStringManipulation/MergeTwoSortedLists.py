def mergeLists(list1, list2):
    new_list = []
    list1_pointer = 0
    list2_pointer = 0
    list1_len = len(list1)
    list2_len = len(list2)

    while ((list1_pointer < list1_len) and (list2_pointer < list2_len)):
        if (list1[list1_pointer] < list2[list2_pointer]):
            new_list.append(list1[list1_pointer])
            list1_pointer += 1

        elif (list2[list2_pointer] < list1[list1_pointer]):
            new_list.append(list2[list2_pointer])
            list2_pointer += 1

        else:
            new_list.append(list1[list1_pointer])
            new_list.append(list2[list2_pointer])
            list2_pointer += 1
            list1_pointer += 1

    while (list1_pointer < list1_len):
        new_list.append(list1[list1_pointer])
        list1_pointer += 1

    while (list2_pointer < list2_len):
        new_list.append(list2[list2_pointer])
        list2_pointer += 1

    print(new_list)


my_list = [3, 4, 6, 10, 11, 15, 20]
alices_list = [1, 5, 8, 12, 15, 19]

mergeLists(my_list, alices_list)
