def valid_anagram(s,t):
    if len(s) != len (t):
        return False
    s_map = {}
    t_map = {}
    for ch in s:
        s_map[ch] = s_map.get(ch, 0) + 1
    for ch in t:
        t_map[ch] = t_map.get(ch, 0) + 1
    return True if s_map == t_map else False

print(valid_anagram("anagram", "nagaram"))