def sqrt_int(n):
    left, right = 0, n
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(sqrt_int(10)) # 3
print(sqrt_int(16)) # 4