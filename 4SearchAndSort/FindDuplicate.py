def find_repeat(numbers):
    lowest = 1
    highest = len(numbers) - 1

    first_half_lower = 1
    first_half_upper = int((highest - 0) / 2)
    second_half_lower = int((highest - 0) / 2) + 1
    second_half_upper = highest
    in_range_numbers = 0

    # print( first_half_lower, first_half_upper, second_half_lower, second_half_upper)
    while(lowest < highest):
        for number in numbers:
            if number >= first_half_lower and number <= first_half_upper:
                in_range_numbers += 1
        if(in_range_numbers > first_half_upper):
            second_half_upper = first_half_upper
            first_half_lower = first_half_lower
            first_half_upper = first_half_lower + int((first_half_upper - first_half_lower) / 2)
            second_half_lower = first_half_upper + 1
        else:
            first_half_lower = second_half_lower
            first_half_upper = second_half_lower + int((second_half_upper - second_half_lower) / 2)
            second_half_lower = first_half_upper + 1
            second_half_upper = second_half_upper
            print(first_half_lower, first_half_upper, second_half_lower, second_half_upper)

        lowest = first_half_lower
        highest = second_half_upper
        in_range_numbers = 0


    print(lowest, highest)
    # print(in_range_numbers)


find_repeat([6,3,4,1,2,5,3])