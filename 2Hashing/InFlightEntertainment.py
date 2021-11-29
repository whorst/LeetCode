def movies(flight_mins, movie_lengths):
    movie_set = set()
    for movie_length in movie_lengths:
        to_find_length = flight_mins - movie_length
        if(to_find_length in movie_set):
            return True
        else:
            movie_set.add(movie_length)
    return False

movies(13, [10, 7, 5, 9, 1, 3])