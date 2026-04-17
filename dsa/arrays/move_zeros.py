# Given an array, move all 0s to the end while maintaining order
# Rules: In-place, Use two pointers, O(n) time

def move_zeros(nums):
    right = 0
    for left in range (len(nums)):
        if nums[left] != 0:
            nums[left],nums[right] = nums[right],nums[left]
            right+=1
nums = [0,1,0,3,12]
move_zeros(nums)
print(nums)