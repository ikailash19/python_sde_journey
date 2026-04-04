# Task 1 - Longest substring with at most K distinc characters
def longest_k_distinct(s, k):
    left = 0
    count = {}
    max_length = 0

    #0,1,2,3,4,
    for right in range(len(s)):
        # {e:2,c:1,b:1},{e:1,b:1,a:1}
        count[s[right]] = count.get(s[right], 0) + 1
        # 1>2x,2>2x,2>2x,3>2->,2>2x,3>2->,2>2x
        while len(count) > k:
            #{e:1,c:1,b:1},{e:1,c:0,b:1}
            #{e:0,b:1,a:1}
            count[s[left]] -= 1
            if count[s[left]] == 0:
                #{e:1,b:1},{b:1,a:1}
                del count[s[left]]
            #left=1,2,3
            left += 1
        #max_length = 1,2,3,3,3
        max_length = max(max_length, right - left + 1)

    return max_length

print(longest_k_distinct("eceba", 2))
###################################################################
# Task 2 - Minimum window substring
# Given: s = "ADOBECODEBANC", t = "ABC"
# Find the smallest substring in s that contains all characters of t

def min_window(s, t):
    if not s or not t:
        return ""
    target = {}
    #target = {A:1,B:1,C:1}
    for ch in t:
        target[ch] = target.get(ch, 0) + 1
    window = {}
    have = 0
    #need = 3
    need = len(target)
    left = 0
    result = ""
    min_len = float("inf")

    #0,1,2,3,4,5,6,7,8,9,10,11,12
    for right in range(len(s)):
        #{A:1,D:1,O:1,B:1,E:1,C:1,N:1}
        window[s[right]] = window.get(s[right], 0 ) + 1

        if s[right] in target and window[s[right]] == target[s[right]]:
            #have=1,2,3,3,3
            have += 1

        #1==3x,1==3x,1==3x,2==3x,2==3x,3==3->2==3x,
        #2==3x,2==3x,2==3x,3==3->,2==3x,3==3->
        while have == need:
            #6<inf->,10<6x,9<6x,8<6x,7<6x,6<6x,6<6x,5<6->,
            if (right - left + 1) < min_len:
                #min_len=6,5,
                min_len = right - left + 1
                #ADOBEC,ODEBANC,
                result = s[left:right+1]
            #{A:0,D:1,O:1,B:1,E:1,C:1},
            #{A:1,D:1,O:2,B:2,E:2,C:1},
            #{A:1,D:1,O:1,B:2,E:2,C:1},
            #{A:1,D:1,O:1,B:1,E:2,C:1},
            #{A:1,D:1,O:1,B:1,E:1,C:1},
            #{A:1,D:1,O:1,B:1,E:1,C:0},
            #{A:1,D:1,O:0,B:1,E:1,C:1,N:1},
            window[s[left]] -= 1

            if s[left] in target and window[s[left]] < target[s[left]]:
                #have=2,2,
                have -= 1
            #left=1,2,3,4,5,6
            left += 1

    return result

print(min_window("ADOBECODEBANC", "ABC")) # BANC
################################################################################

























