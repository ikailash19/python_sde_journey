# Task 1 - Palindrome Check
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("madam")) # True
print(is_palindrome("hello")) # False
##################################################
# Task 2 - Reverse String using two pointers
def reverse_string(s):
    s = list(s) # Strings are immutable in Python
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

print(reverse_string("python")) #nohtyp
##################################################
# Task 3 - Anagram Check
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False
    return True

print(is_anagram("listen", "silent")) # True
print(is_anagram("hello", "world")) # False