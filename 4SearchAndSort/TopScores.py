def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    number_of_scores = len(unsorted_scores)
    count_array = [0] * (HIGHEST_POSSIBLE_SCORE + 1)
    # print(count_array)

    for number in unsorted_scores:
        count_array[number] = count_array[number] + 1

    x = len(count_array) - 1
    scores_iter = 0
    while x > -1:
        if count_array[x] != 0:
            unsorted_scores[scores_iter] = x
            scores_iter += 1
        x-=1

    return (unsorted_scores)



unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))