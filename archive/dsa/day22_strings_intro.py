# Task - Character frequency
def char_frequency(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("automation"))
# {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}
##########################################################
# Task - First non-repeating character
def first_unique_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

print(first_unique_char("automation")) # u