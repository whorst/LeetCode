def mergeMeetingTimes(times):
    new_times = []
    new_times.append(times[0])
    new_times_prev = 0

    for time in times[1:]:
        if(time[0] <= new_times[new_times_prev][1]):
            new_tuple = (new_times[new_times_prev][0], time[1])
            new_times[new_times_prev] = new_tuple
        else:
            new_times.append(time)
            new_times_prev +=1
    print(new_times)



def mergeSort(times):
    if (len(times) > 1):
        middle = int(len(times) // 2)

        left = times[:middle]
        right = times[middle:]

        mergeSort(left)
        mergeSort(right)
        sort(left, right, times)


def sort(left, right, times_l):
    left_iter = 0
    right_iter = 0
    times_iter = 0
    while (left_iter < len(left) and right_iter < len(right)):
        if (left[left_iter][0] < right[right_iter][0]):
            times_l[times_iter] = (left[left_iter])
            left_iter += 1

        else:
            times_l[times_iter] = (right[right_iter])
            right_iter += 1
        times_iter += 1

    while (left_iter < len(left)):
        times_l[times_iter] = (left[left_iter])
        left_iter += 1
        times_iter+=1

    while (right_iter < len(right)):
        times_l[times_iter] = (right[right_iter])
        right_iter += 1
        times_iter+=1

times = [(3, 5), (10, 12), (9, 10), (4, 8), (0, 1)]
g = [4, 6, 3, 5, 8, 4, 2, 5, 7, 9, 5, 2, 5, 7]
mergeSort(times)
mergeMeetingTimes(times)
