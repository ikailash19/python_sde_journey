# Find indices of two numbers that sum to target
# Rules: No nested loops, use hashmap
def two_sum(nums, target):
    hash_map = {}
    for i in range (len(nums)):
        needed = target - nums[i]
        if needed in hash_map:
            return [hash_map[needed], i]
        hash_map[nums[i]] = i
    return -1

print(two_sum([1,4,2,7,5,8,7], 11))