# Task - Sorted array -> Remove duplicates in place
def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1

arr = [1,1,2,2,3,4,4]
length = remove_duplicates(arr)

print(length)
print(arr[:length])