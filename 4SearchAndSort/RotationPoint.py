def rotationPoint(rotated_list, start, end):

    if(rotated_list[start] < rotated_list[end]):
        return start
    diff = end -start
    if(diff <= 4):
        if(rotated_list[start] < rotated_list[end]):
            return start
        else:
            prev = start
            current = start +1
            while current <= end:
                if(rotated_list[prev] > rotated_list[current]):
                    return current
                current +=1
                prev+=1

    first_half_start = start
    first_half_end = int((end - start) / 2 + start)
    second_half_start = int((end - start) / 2 + start) + 1
    second_half_end = end

    if (rotated_list[first_half_start] > rotated_list[first_half_end]):
        return rotationPoint(rotated_list, first_half_start, first_half_end)

    elif (rotated_list[second_half_start] > rotated_list[second_half_end]):
        return rotationPoint(rotated_list, second_half_start, second_half_end)
    elif(rotated_list[first_half_end] > rotated_list[second_half_start]):
        return second_half_start


rotated_list = ["e", "f", "g", "h", "i", "j", "a", "b", "c"]
rotated_list = [
'ptolemaic',
'retrograde',
'supplant',
'undulate',
'xenoepist',
'asymptote',  # <-- rotates here!
'babka',
'banoffee',
'engender',
'karpatka',
'othellolagkage',
]
print(rotated_list[rotationPoint(rotated_list, 0, len(rotated_list) - 1)])