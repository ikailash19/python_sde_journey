def sqrt_ceil(n):
    left, right = 0, n
    answer = n

    while left <= right:
        mid = (left + right) // 2

        if mid * mid >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

print(sqrt_ceil(10)) # 4
print(sqrt_ceil(16)) # 4