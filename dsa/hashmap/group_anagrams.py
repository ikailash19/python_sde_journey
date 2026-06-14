def group_anagrams(words):
    hash_map = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word not in hash_map:
            hash_map[sorted_word] = []

        hash_map[sorted_word].append(word)

    return list(hash_map.values())

print(group_anagrams(["eat", "tea", "tan",
                      "ate", "nat", "bat"]))

# Time complexity: O(n * k log k)
# n -> number of words
# k log k for every sorted()
# where k is length of each word to be sorted

# Space complexity: O(n * k)
