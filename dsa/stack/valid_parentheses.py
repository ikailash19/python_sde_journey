def valid_parentheses(string):
    pairs = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    stack = []
    for char in string:
        if(char in pairs):
            if not stack:
                return False
            popped = stack.pop()
            if not popped == pairs.get(char):
                return False
        else:
            stack.append(char)

    return len(stack) == 0

print(valid_parentheses("([]{}"))