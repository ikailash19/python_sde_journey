def longest_common_prefix(strs):
    if not strs:
        return ""
    common = strs[0]
    for string in strs[1:]:
        limit = min(len(common), len(string))
        for i in range (limit):
            prefix_length = limit
            if common[i] != string[i]:
                prefix_length = i
                break
        common = common[:prefix_length]
    return common

print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))