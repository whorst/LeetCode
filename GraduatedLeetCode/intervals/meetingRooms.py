def meetingRooms(meetingRooms):
    meeting_dict = {}
    meeting_dict[1] = [meetingRooms[0]]
    highest_meeting_room = 1

    for meeting in range(1, len(meetingRooms)):


        # if highest_meeting_room == 1:
        #     highest_meeting_room = check_prev_meetings(1, meeting, meetingRooms, meeting_dict,
        #                                                meeting_end, meeting_start)
        #
        # else:
        highest_meeting_room = check_prev_meetings(highest_meeting_room, meeting, meetingRooms, meeting_dict)
    print(meeting_dict)


def check_prev_meetings(highest_meeting_room, meeting, meetingRooms, meeting_dict):
    meeting_start = meetingRooms[meeting][0]
    meeting_end = meetingRooms[meeting][1]
    is_added = False
    for i in range(1, highest_meeting_room + 1):
        if is_added:
            break
        can_add = True
        for prev_meeting in meeting_dict.get(i):
            prev_meeting_start = prev_meeting[0]
            prev_meeting_end = prev_meeting[1]
            if prev_meeting_start < meeting_start < prev_meeting_end or prev_meeting_start < meeting_end < prev_meeting_end or (
                    meeting_start < prev_meeting_start and meeting_end > prev_meeting_end):
                can_add = False
                break
        if can_add:
            meeting_dict[i].append(meetingRooms[meeting])
            is_added = True
    if (not is_added):
        highest_meeting_room += 1
        meeting_dict[highest_meeting_room] = [meetingRooms[meeting]]
    return highest_meeting_room


# meetingRooms([(0,30), (5,10), (15,20), (0,20)])
meetingRooms([[1, 18],
            [18, 23],
            [15, 29],
            [4, 15],
            [2, 11],
            [5, 13],
      ])

# Problem Description
#
# Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.
#
# Where:
#
# A[i][0] = start time of the ith meeting.
# A[i][1] = end time of the ith meeting.
# Find the minimum number of conference rooms required so that all meetings can be done.
#
#
#
# Problem Constraints
# 1 <= N <= 10
#
# 0 <= A[i][0] < A[i][1] <= 2 * 109
#
#
#
# Input Format
# The only argument given is the matrix A.
#
#
#
# Output Format
# Return the minimum number of conference rooms required so that all meetings can be done.
#
#
#
# Example Input
# Input 1:
#
#  A = [      [0, 30]
#             [5, 10]
#             [15, 20]
#      ]
#
# Input 2:
#
#  A =  [     [1, 18]
#             [18, 23]
#             [15, 29]
#             [4, 15]
#             [2, 11]
#             [5, 13]
#       ]