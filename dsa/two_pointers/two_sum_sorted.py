def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        else:
            left += 1
    return "Sum not found"

print(two_sum_sorted([2,7,11,15], 9))