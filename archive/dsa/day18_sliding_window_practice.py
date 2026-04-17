# Slot 1 - Sliding Window Reinforcement
# Task - Maximum Sum Subarray of Size K
def sliding_window_sum(arr, k):
    max_sum = frame = sum(arr[:k])
    for index in range(k, len(arr)):
        frame += arr[index]
        frame -= arr[index - k]
        if frame > max_sum:
            max_sum = frame

    return max_sum
print(sliding_window_sum([2,1,5,1,3,2], 3))