cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20

def bad_max_duffel_bag_value(cake_tuples, capacity):
    if capacity == 0:
        for thing in cake_tuples:
            if thing[0] == 0:
                return float('inf')
        return 0
    else:
        cake_set = set()
        brute_force_find_largest(capacity, 0, cake_set, cake_tuples)
        highest = 0
        for val in cake_set:
            if val > highest:
                highest = val
        return highest
        # return cake_set

def brute_force_find_largest(weight_remaining, value, cake_set, cake_tuples):
    for tuple in cake_tuples:
        if weight_remaining - tuple[0] > -1:
            brute_force_find_largest(weight_remaining-tuple[0], value + tuple[1], cake_set, cake_tuples)
        else:
            cake_set.add(value)

def max_duffel_bag_value(cake_tuples, capacity):
    value_cache = [None] * (capacity + 1)
    min_weight = None
    # print(value_cache)

    for cake_tuple in cake_tuples:
        if min_weight == None:
            min_weight = cake_tuple[0]
        else:
            min_weight = min(min_weight, cake_tuple[0])
        value_cache[cake_tuple[0]] = cake_tuple[1]
    print(value_cache)
    prev_value = -1

    for curr_weight in range(min_weight, capacity+1):
        for tuple in cake_tuples:
            tuple_weight, tuple_value = tuple[0], tuple[1]
            if tuple_weight <= curr_weight:
                remainder_weight = curr_weight - tuple_weight
                remainder_value = value_cache[remainder_weight]
                if remainder_value != None:
                    total_value = tuple_value + remainder_value
                    if value_cache[curr_weight] == None:
                        value_cache[curr_weight] = max(total_value, prev_value)
                    else:
                        value_cache[curr_weight] = max(value_cache[curr_weight], total_value, prev_value)
                    prev_value = value_cache[curr_weight]
                else:
                    if value_cache[curr_weight] == None:
                        value_cache[curr_weight] = max(tuple_weight, prev_value)
                    else:
                        value_cache[curr_weight] = max(value_cache[curr_weight], prev_value)
                    prev_value = value_cache[curr_weight]

    return value_cache
    #
    # return value_cache[capacity]

#Cakes can weigh nothing, duffle bags can hold nothing

# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
# x = bad_max_duffel_bag_value(cake_tuples, capacity)
# print(x)

print(max_duffel_bag_value(cake_tuples, capacity))
