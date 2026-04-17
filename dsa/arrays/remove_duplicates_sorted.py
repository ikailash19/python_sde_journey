# Remove duplicates from sorted array (in-place)
def remove_duplicates_sorted(arr):
    if not arr:
        return []
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1
    return arr[:write]

print(remove_duplicates_sorted([1,2,4,4,5,7,7,9]))