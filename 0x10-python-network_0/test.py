#!/usr/bin/python3
def find_peak(list_of_integers):
    left, right = 0, len(list_of_integers) - 1
    if len(list_of_integers) == 0:
        return None
    while left < right:
        mid = (left + right)//2
        if list_of_integers[mid] > list_of_integers[mid+1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
