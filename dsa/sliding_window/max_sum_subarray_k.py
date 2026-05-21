def max_sum_subarray_k(nums, k):
    left = 0
    current_window = max_sum = sum(nums[:k])
    for right in range(k, len(nums)):
        current_window += nums[right]
        current_window -= nums[left]
        left += 1
        if max_sum < current_window:
            max_sum = current_window
    return max_sum

print(max_sum_subarray_k([2,1,5,1,3,2], 3))