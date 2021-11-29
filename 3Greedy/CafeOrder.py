def cafe_order(take_out, dine_in, served):
    take_out_pointer = dine_in_pointer = 0

    for item in served:
        if (take_out_pointer < len(take_out) and item == take_out[take_out_pointer]):
            take_out_pointer += 1
        elif (dine_in_pointer < len(dine_in) and item == dine_in[dine_in_pointer]):
            dine_in_pointer += 1
        else:
            return False
    return True


take_out = [17, 8, 24]
dine_in = [12, 19, 2]
served = [17, 8, 12, 19, 24, 2]

print(cafe_order(take_out, dine_in, served))