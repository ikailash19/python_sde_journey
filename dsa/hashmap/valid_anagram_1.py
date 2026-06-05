def valid_anagram_1(s,t):
    return False if len(s) != len(t) else True

    s_map = {}
    t_map = {}

    for char in s:
        s_map[char] = s_map.get(char, 0) + 1

    for char in t:
        t_map[char] = t_map.get(char, 0) + 1

    return s_map == t_map

print(valid_anagram_1("anagram", "nagaram"))