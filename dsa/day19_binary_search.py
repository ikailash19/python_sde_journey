# Task 1 - Basic Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    #0 <= 6, 4 <= 6, 4 <= 4
    while left <= right:
        # mid = 3, 5, 4
        mid = (left + right) // 2

        # 4 == 5, 6 == 5, 5 == 5
        if arr[mid] == target:
            # 4
            return mid
        # 4 < 5, 6 < 5
        elif arr[mid] < target:
            # left = 4
            left = mid + 1
        else:
            # right = 4
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7], 5)) #4
print(binary_search([1, 2, 3, 4, 5, 6, 7], 10)) #-1

##########################################################
# Task 2 - First Occurrence
def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    # 0<=5, 0<=1, 1<=1, 1<=0x
    while left <= right:
        # mid = 2, 0, 1
        mid = (left + right) // 2

        # 2 == 2, 1 == 2, 2 == 2
        if arr[mid] == target:
            # answer = 2, 1
            answer = mid
            # right = 1, 0
            right = mid - 1
        # 1 < 2
        elif arr[mid] < target:
            # left = 1
            left = mid + 1
        else:
            right = mid - 1
    return answer

print(first_occurrence([1, 2, 2, 2, 3, 4], 2)) #1
print(first_occurrence([2, 2, 2, 2], 2)) #0
print(first_occurrence([1, 3, 5, 7], 2)) #-1