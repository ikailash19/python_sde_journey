def two_sum_1(nums, target):
    sum_map = {}
    for i in range(len(nums)):
        needed_value = target - nums[i]

        if needed_value in sum_map:
            return [sum_map.get(needed_value), i]
        sum_map[nums[i]] = i

    return False

print(two_sum_1([2,7,11,15],9))