# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # : List[ListNode])
    def mergeKLists(self, lists) -> ListNode:

        if (len(lists) == 0):
            return ListNode("")

        max_val = None
        min_val = None
        bucket = {}
        for l in lists:
            curr_val = l
            while curr_val != None:
                current_val = curr_val.val
                if (max_val == None or min_val == None):
                    max_val = current_val
                    min_val = current_val
                if (current_val > max_val):
                    max_val = current_val
                if (current_val < min_val):
                    min_val = current_val
                if bucket.get(current_val) == None:
                    bucket[current_val] = [curr_val]
                else:
                    bucket[current_val].append(curr_val)
                curr_val = curr_val.next

        new_list = None

        curr = None
        if (max_val == None or min_val == None):
            return ListNode("")

        for x in range(min_val, max_val + 1):
            if bucket.get(x):
                for node in bucket.get(x):
                    if curr == None:
                        curr = node
                        new_list = curr
                    else:
                        curr.next = node
                        curr = curr.next
        if new_list:
            return new_list
        else:
            ListNode("", None)