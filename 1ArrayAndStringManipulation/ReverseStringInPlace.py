def reverseInPlace(input):
    front_pointer = 0
    back_pointer = len(input) - 1
    while (True):
        if(front_pointer > back_pointer or front_pointer==back_pointer):
            return
        temp = input[front_pointer]
        input[front_pointer] = input[back_pointer]
        input[back_pointer] = temp

        front_pointer += 1
        back_pointer -= 1

l = ["a", "g", "f", "d", "e", "b", "n", "c"]
reverseInPlace(l)
print(l)
# n, b,  e,  d,  f,  g,  a
