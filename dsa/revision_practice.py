# Day 24 - Revision
# Revise 1 - Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    #0<=6,4<=6,4<=4,
    while left <= right:
        #mid = 3,5,4
        mid = (left + right) // 2
        #3==4x,5==4x,4==4
        if arr[mid] == target:
            return mid
        #3<4,5<4x
        elif arr[mid] < target:
            #left = 4,
            left = mid + 1
        else:
            #right = 4,
            right = mid - 1
    return -1
print(binary_search([1, 2, 2, 3, 4, 5, 6], 4)) # 4
##############################################################
# Revise 2 - Binary Search First occurrence
def binary_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    answer = -1
    #0<=6, 0<=2, 2<=2, 2<=1x
    while left <= right:
        #mid = 3,1,2,
        mid = (left + right) // 2
        #3==3,2==3,3==3,
        if arr[mid] == target:
            #answer=3,2
            answer = mid
            #right=2,1
            right = mid - 1
        #2<3
        elif arr[mid] < target:
            #left=2
            left = mid + 1
        else:
            right = mid - 1
    return answer
print(binary_first_occurrence([1, 2, 3, 3, 3, 4, 4, 5], 3)) # 2
##########################################################################
# Revise 3 - Sliding window fixed sum
def max_window_sum(arr, k):
    max_window = sum(arr[:k])
    window_frame = max_window

    for index in range(k, len(arr)):
        window_frame += arr[index]
        window_frame -= arr[index - k]
        if window_frame > max_window:
            max_window = window_frame
    return max_window
print(max_window_sum([2, 1, 5, 3, 7], 3)) # 15
#########################################################################
#########################################################################
# Day 25 - Revision
# Revise 1 - Longest Unique substrings
def longest_unique_substring(s):
    max_length = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_unique_substring('abacdaea')) # 4
########################################################################
# Revise 2 - Count Unique substring
def count_unique_substring(s):
    unique_count = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        unique_count += right - left + 1
    return unique_count

print(count_unique_substring('abacdaea')) # 21
#############################################################
#############################################################
# Day 26 - Revision
# Task 1 - Longest Unique Substring
def longest_unique_substrings(s):
    seen = set()
    max_length = 0
    left = 0
    #0,1,2,3,
    for right in range(len(s)):
        #a in x,b in x,c in x, b in ->,
        # b in ->,
        while s[right] in seen:
            #(b,c),(c),
            seen.remove(s[left])
            #left = 1,2
            left += 1
        #(a,b,c),(c,b,
        seen.add(s[right])
        #max_length=1,2,3,3,
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_unique_substring("abcbdace")) # 5
########################################################################
# Task 2 - Count Unique Substrings
def unique_substrings(s):
    unique_count = 0
    left = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        unique_count += right - left + 1
    return unique_count
print(unique_substrings('abacdaea')) # 21
######################################################################
######################################################################
# Day 26 - Revision
# Task 1 - Minimum window substring
# Given: s = "ADOBECODEBANC", t = "ABC"
# Find the smallest substring in s that contains all characters of t

def min_window(s, t):
    result = "None"
    left = 0
    have = 0
    need = len(t)
    target = {}
    window = {}
    for char in t:
        target[char] = target.get(char, 0) + 1
    min_length = float("inf")

    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1

        if s[right] in target and window[s[right]] == target[s[right]]:
            have += 1

        while have == need:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                result = s[left:right+1]

            window[s[left]] -= 1

            if s[left] in target and window[s[left]] < target[s[left]]:
                have -= 1
            left += 1

    return result

print(min_window("ADOBECODEBANC", "ABC"))
######################################################################
######################################################################
# Day 27 - Revision
# Task 1 - Minimum window substring
# Given: s = "ADOBECODEBANC", t = "ABC"
# Find the smallest substring in s that contains all characters of t

def min_window_2(string,t):
    left = 0
    min_length = float("inf")
    result = ""
    target = {}
    window = {}
    have = 0
    need = len(t)
    for char in t:
        target[char] = target.get(char, 0) + 1

    for right in range(len(string)):
        window[string[right]] = window.get(string[right], 0) + 1

        if string[right] in target and window[string[right]] == target[string[right]]:
            have += 1

        while have == need:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                result = string[left : right + 1]

            window[string[left]] -= 1

            if string[left] in target and window[string[left]] < target[string[left]]:
                have -= 1

            left += 1
    return result

print(min_window_2("ADOBECODEBANC", "ABC"))
################################################################################################
################################################################################################
# Day 28 - Revision
# Task 1 - Longest Repeating Character Replacement
def longest_repeating_replacement(s,k):
    max_length = 0
    left = 0
    window = {}
    max_freq = 0

    for right in range (len(s)):
        window[s[right]] = window.get(s[right], 0) + 1
        max_freq = max(max_freq, window[s[right]])
        while ((right - left + 1) - max_freq) > k:
            window[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_repeating_replacement("ABAACDA", 1)) # 4
#################################################################################################
# Task 2 - Longest string with k distinct
def longest_k_distinct(s,k):
    left = 0
    count = {}
    max_length = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_k_distinct("BCBBBBDBBBBBBBBBBE",3)) # 17
##################################################################################################
# Task 3 - Min window
def min_window_3(s,t):
    result = ""
    target = {}
    window = {}
    min_length = float("inf")
    left = 0
    have = 0
    for char in t:
        target[char] = target.get(char, 0) + 1
    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1

        if s[right] in target and window[s[right]] == target[s[right]]:
            have += 1

        while have == len(target):
            if min_length > (right - left + 1):
                min_length = right - left + 1
                result = s[left:right+1]

            window[s[left]] -= 1

            if s[left] in target and window[s[left]] < target[s[left]]:
                have -= 1
            left += 1
    return result

print(min_window_3("AJOSFAIICMFAWD", "AMIF"))
####################################################################################
####################################################################################


