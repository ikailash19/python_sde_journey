# Task 1 - Longest Repeating Character Replacement
def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0
    #0,1,2,3,4,5,6
    for right in range(len(s)):
        #{A:1},{A:2},{A:2,B:1},{A:3,B:1},{A:3,B:2},
        #{A:2,B:3},{A:2,B:3}
        count[s[right]] = count.get(s[right], 0) + 1
        #max_freq=1,2,2,3,3,3,3
        max_freq = max(max_freq, count[s[right]])

        # 0>1x,0>1x,1>1x,1>1x,2>1->,1>1x,2>1->,1>1x,
        # 2>1->,
        while (right - left + 1) - max_freq > k:
            #{A:2,B:2},{A:1,B:3},{A:2,B:2},
            count[s[left]] -= 1
            #left=1,2,3
            left += 1
        #max_length=1,2,3,4,4,4,4
        max_length = max(max_length, right - left + 1)

    return max_length

print(character_replacement("AABABBA", 1)) #4
################################################################
# Task 2 - Max consecutive 1s with at most k flips
def max_consecutive_ones(arr, k):
    zero_count = 0
    left = 0
    max_length = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            zero_count += 1
        while zero_count > k:
            if arr[left] == 0:
                zero_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(max_consecutive_ones([1,1,0,0,1,1,1,0], 2)) # 7