def top_k_frequent_elements(nums, k):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
    sorted_dict = sorted(hash_map.items(),key=lambda pair : pair[1], reverse=True)
    return [pair[0] for pair in sorted_dict[:k]]

print(top_k_frequent_elements([5,5,5,5,1,2,2], 1))

# Time complexity: O(n log n)
# Space complexity: O(n)