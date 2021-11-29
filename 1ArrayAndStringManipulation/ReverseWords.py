def reverseSentence(sentence_arr):
    to_insert = step = 0
    arr_len = len(sentence_arr)
    last_index = arr_len - 1

    while(step<arr_len):
        last_letter = sentence_arr.pop(last_index)
        if(last_letter == ' '):
            to_insert = step
            sentence_arr.insert(to_insert, last_letter)
            to_insert = to_insert +1
        else:
            sentence_arr.insert(to_insert, last_letter)
        step=step+1

    print(sentence_arr)

def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1

message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]

reverse_words(message)