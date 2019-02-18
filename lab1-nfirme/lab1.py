def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

    # checks if int_list is empty or None
    if int_list is None:
        raise ValueError

    if not int_list:
        return None

    # sets max equal to first value in list
    # iterates through list
    # if value is greater than max, sets max equal to that value

    max = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > max:
            max = int_list[i]
    return max


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    # if list is empty, return the list
    if len(int_list) < 1:
        return int_list
    # return the last value in the list, then add the called new list
    return [int_list[-1]] + reverse_rec(int_list[0:-1])



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError

    if target in int_list: # checks if target is in list, returns None if false
        mid = int((low + high) / 2) # sets mid to lists's middle (average) value

        if int_list[mid] == target: # if target is in mid index, return mid index
            return mid
        elif int_list[mid] < target: # if target is to the left of mid, gets rid of right half then calls function again
            return bin_search(target, mid + 1, high, int_list)
        else: # if target is to right of mid, gets rid of left half
            return bin_search(target, low, mid - 1, int_list)
    else:
        return None
