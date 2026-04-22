def product_of_array(nums):
    suffix = [1] * len(nums)
    prefix = [1] * len(nums)
    result = [None] * len(nums)

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    for i in range(len(nums)):
        result[i] = prefix[i] * suffix[i]
    return result

def product_of_array_v2(nums):
    prefix = 1
    suffix = 1
    result = [1] * len(nums)
    for i in range (len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
print(product_of_array_v2([1,2,3,4]))
print(product_of_array([1,2,3,4]))
