def fib(number):

    if number == 1:
        return 0
    if number == 2:
        return 1

    iterator = 3

    prev_prev = 0
    prev = 1
    curr = -1


    while iterator <= number:
        curr = prev + prev_prev
        prev_prev = prev
        prev = curr
        iterator +=1

    return curr


print(fib(7))