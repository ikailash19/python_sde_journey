def subarray_sum(nums, k):
    total = 0
    for i in range (len(nums)):
        current_sum = 0
        for j in range(i,len(nums)):
            current_sum += nums[j]
            if current_sum == k:
                total += 1
    return total

print(subarray_sum([1,1,1], 2))