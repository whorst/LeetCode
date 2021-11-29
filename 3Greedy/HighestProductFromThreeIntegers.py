def three_ints(list_of_ints):
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_two = highest * lowest
    lowest_product_of_two = highest_product_of_two
    highest_product_of_three = max(highest_product_of_two * list_of_ints[2], lowest_product_of_two * list_of_ints[2])
    lowest_product_of_three = min(highest_product_of_two * list_of_ints[2], lowest_product_of_two * list_of_ints[2])

    # highest = max(highest, list_of_ints[2])
    # lowest = min(lowest, list_of_ints[2])

    for current in list_of_ints[2:]:
        # highest_product_of_two = max(current * highest, current * lowest, highest * lowest, highest_product_of_two)
        # lowest_product_of_two = min(current * highest, current * lowest, highest * lowest, lowest_product_of_two)

        highest_product_of_three = max(current * highest_product_of_two, highest_product_of_three, current * lowest_product_of_two)
        lowest_product_of_three = min(current * highest_product_of_two, lowest_product_of_three, current * lowest_product_of_two)

        highest_product_of_two = max(current * highest, current * lowest, highest * lowest, highest_product_of_two)
        lowest_product_of_two = min(current * highest, current * lowest, highest * lowest, lowest_product_of_two)

        highest = max(current, highest)
        lowest = min(current, lowest)
    return highest_product_of_three

list_of_ints = [1, 10, -5, 1, 16,24,6267,40,19,69,50,-33,21,7,-100]
print(three_ints(list_of_ints))
