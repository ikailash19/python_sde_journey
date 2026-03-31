# Task - Longest substring without repeating characters
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0

    # right= 0,1,2,3,4,5,6,7
    for right in range(len(s)):
        # a in x, b in x, c in x, a in ->, a in x,
        # b in ->, b in x, c in ->, c in x, b in ->,
        # b in ->, b in x, b in ->, b in ->, b in x
        while s[right] in seen:
            #(b,c), (c,a), (a,b),(b,c),(c),(b),()
            seen.remove(s[left])
            #left=1,2,3,4,5,6,7
            left += 1
        #seen=(a,b,c),(b,c,a),(c,a,b),(a,b,c),
        #(c,b),(b)
        seen.add(s[right])
        #max_length=1,2,3,3,3,3,3,3
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_unique_substring("abcabcbb")) # 3
print(longest_unique_substring("bbbbb"))    # 1
print(longest_unique_substring("pwwkew"))   # 3
#######################################################################
# Task - Count substrings with no repeating characters
def unique_substrings(s):
    seen = set()
    left = 0
    unique_count = 0
    #right=0,1,2,3,4,5,6,7
    for right in range(len(s)):
        # a in x, a in ->, a in x, b in x, b in ->,
        # b in ->, b in x, c in x, c in ->, c in ->,
        # c in x, d in x, d in ->, d in ->,
        while s[right] in seen:
            #(),(b),(),(c),(),(d),()
            seen.remove(s[left])
            #left=1,2,3,4,5,6,7
            left += 1
        #(a),(a,b),(b,c),(c,d),(d)
        seen.add(s[right])
        # unique_count=1,2,4,5,7,8,10,11
        unique_count += (right - left + 1)
    return unique_count

print(unique_substrings("aabbccdd")) # 11
print(unique_substrings("abc")) # 6
print(unique_substrings("aa")) # 2