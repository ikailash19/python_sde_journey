def longest_repeating_character(s,k):
    characters = {}
    max_length = 0
    max_frequency = 0
    left = 0
    for right in range(len(s)):
        characters[s[right]] = characters.get(s[right], 0) + 1
        max_frequency = max(characters[s[right]], max_frequency)
        while (right - left + 1) - max_frequency > k:
            characters[s[left]] -= 1
            if characters[s[left]] == 0:
                del characters[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length

print(longest_repeating_character("AABABBA", 1))