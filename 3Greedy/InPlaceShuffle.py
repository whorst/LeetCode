import random



def inPlaceShuffle(list_to_shuffle):
    pointer = 0
    while(pointer < len(list_to_shuffle)):
        random_number = random.randint(0, len(list_to_shuffle)-1)
        place = list_to_shuffle[pointer]
        list_to_shuffle[pointer] = list_to_shuffle[random_number]
        list_to_shuffle[random_number] = place
        pointer += 1


    return list_to_shuffle


list_to_shuffle = [1,2,3,4,5]
print(list_to_shuffle)
print(inPlaceShuffle(list_to_shuffle))
