def valid_palindrome(string):
    left = 0
    right = len(string) - 1
    while(left < right):
        if(string[left].lower() != string[right].lower()):
            if not string[left].isalpha():
                left += 1
                continue
            elif not string[right].isalpha():
                right -= 1
                continue
            else:
                return False
        left += 1
        right -= 1
    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))
