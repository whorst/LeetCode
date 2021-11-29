def count(amount, denomination):
    totals = [0] * (amount + 1)
    totals[0] = 1

    for denom in denomination:
        for numb in range(1, amount + 1):
            if numb >= denom:
                remainder = numb - denom
                totals[numb] += totals[remainder]

    return totals


print(count(6, [2, 4]))
# print(change_possibilities_bottom_up(5, [2,3]))
