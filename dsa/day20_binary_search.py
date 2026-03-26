# Task 1 - Last Occurrence
def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    # 0<=5, 3 <=5, 3<=3, 4<=3x
    while left <= right:
        # 2, 4, 3
        mid = (left + right) // 2

        # 2 == 2, 3==2, 2==2
        if arr[mid] == target:
            # 2, 3
            answer = mid
            # left = 3, 4
            left = mid + 1
        # 3<2
        elif arr[mid] < target:
            left = mid + 1
        else:
            # right = 3
            right = mid - 1

    return answer

print(last_occurrence([1, 2, 2, 2, 3, 4], 2)) # 3
#############################################################
# Task - First Occurrence
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
#############################################################
# Task 2 - Count occurrences
def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)

    if first == -1:
        return 0

    return last - first + 1

print(count_occurrences([1, 2, 2, 2, 3, 4], 2)) # 3