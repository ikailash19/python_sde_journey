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

def subarray_sum_optimized(nums, k):
    subarray_sums = {0:1}
    current_sum = 0
    count = 0
    for i in range (len(nums)):
        current_sum += nums[i]
        if current_sum - k in subarray_sums:
            count += subarray_sums[current_sum - k]
        subarray_sums[current_sum] = subarray_sums.get(current_sum, 0) + 1
    return count
print(subarray_sum_optimized([1,2,3,3,6,9],3))

def subarray_sum_optimized_v2(nums, k):
    subarray_sums = {0:1}
    count = 0
    current_sum = 0
    for i in range (len(nums)):
        current_sum += nums[i]
        if current_sum - k in subarray_sums:
            count += subarray_sums[current_sum - k]
        subarray_sums[current_sum] = subarray_sums.get(current_sum, 0) + 1
    return count
print(subarray_sum_optimized_v2([1,2,3,3,6,9], 3))














