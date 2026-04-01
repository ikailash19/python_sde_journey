# Day 24 - Revision
# Revise 1 - Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    #0<=6,4<=6,4<=4,
    while left <= right:
        #mid = 3,5,4
        mid = (left + right) // 2
        #3==4x,5==4x,4==4
        if arr[mid] == target:
            return mid
        #3<4,5<4x
        elif arr[mid] < target:
            #left = 4,
            left = mid + 1
        else:
            #right = 4,
            right = mid - 1
    return -1
print(binary_search([1, 2, 2, 3, 4, 5, 6], 4)) # 4
##############################################################
# Revise 2 - Binary Search First occurrence
def binary_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    answer = -1
    #0<=6, 0<=2, 2<=2, 2<=1x
    while left <= right:
        #mid = 3,1,2,
        mid = (left + right) // 2
        #3==3,2==3,3==3,
        if arr[mid] == target:
            #answer=3,2
            answer = mid
            #right=2,1
            right = mid - 1
        #2<3
        elif arr[mid] < target:
            #left=2
            left = mid + 1
        else:
            right = mid - 1
    return answer
print(binary_first_occurrence([1, 2, 3, 3, 3, 4, 4, 5], 3)) # 2
##########################################################################
# Revise 3 - Sliding window fixed sum
def max_window_sum(arr, k):
    max_window = sum(arr[:k])
    window_frame = max_window

    for index in range(k, len(arr)):
        window_frame += arr[index]
        window_frame -= arr[index - k]
        if window_frame > max_window:
            max_window = window_frame
    return max_window
print(max_window_sum([2, 1, 5, 3, 7], 3)) # 15
#########################################################################
#########################################################################
# Day 25 - Revision
# Revise 1 - Longest Unique substrings
def longest_unique_substring(s):
    max_length = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_unique_substring('abacdaea')) # 4
########################################################################
# Revise 2 - Count Unique substring
def count_unique_substring(s):
    unique_count = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        unique_count += right - left + 1
    return unique_count

print(count_unique_substring('abacdaea')) # 21
#############################################################
#############################################################