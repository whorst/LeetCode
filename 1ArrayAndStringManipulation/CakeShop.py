def areOrdersSequential(dine_in, take_out, served_orders):
    dine_in_index = 0
    take_out_index = 0
    served_order_index = 0
    dine_in_max = len(dine_in)
    take_out_max = len(take_out)

    while ((dine_in_index < dine_in_max) and (take_out_index < take_out_max)):
        if(dine_in[dine_in_index] == served_orders[served_order_index]):
            dine_in_index += 1
            served_order_index += 1
        elif(take_out[take_out_index] == served_orders[served_order_index]):
            take_out_index += 1
            served_order_index += 1
        else:
            return False

    while(dine_in_index < dine_in_max):
        if (dine_in[dine_in_index] != served_orders[served_order_index]):
            return False
        dine_in_index += 1
        served_order_index += 1

    while(take_out_index < take_out_max):
        if (take_out[take_out_index] != served_orders[served_order_index]):
            return False
        take_out_index += 1
        served_order_index += 1
    return True


take_out = [1, 3, 5]
dine_in = [2, 4, 6]
served = [1, 2, 4, 3, 6, 5]

take_out = [17, 8, 24]
dine_in = [12, 19, 2]
served = [17, 8, 12, 19, 24, 2]


print(areOrdersSequential(dine_in, take_out, served))
