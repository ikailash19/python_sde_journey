def permutation_in_string(s1, s2):
    s1_map = {}
    window_map = {}
    left = 0
    for s in s1:
        s1_map[s] = s1_map.get(s, 0) + 1
    for right in range(len(s2)):
        window_map[s2[right]] = window_map.get(s2[right], 0) + 1
        while (right - left + 1) > len(s1):
            window_map[s2[left]] -= 1
            if window_map[s2[left]] == 0:
                window_map.pop(s2[left])
            left += 1
        if window_map == s1_map:
            return True
    return False

print(permutation_in_string("ab", "eidbaooo"))
print(permutation_in_string("ab", "eidboaooo"))
print(permutation_in_string("ab", "bbbbba"))