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

def two_sum_v2(arr,target):
    hash_map = {}
    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in hash_map:
            return [hash_map.get(needed), i]
        hash_map[arr[i]] = i
    return -1
print(two_sum_v2([1,2,5,6,8,9,4], 14))









