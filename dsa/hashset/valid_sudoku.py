def valid_sudoku(string):
    hashset = set()
    for char in string:
        if not char == ".":
            if char in hashset:
                return False
            else:
                hashset.add(char)
    return True

print(valid_sudoku([
    "5",
    "3",
    ".",
    ".",
    "7",
    ".",
    "8",
    ".",
    "."
]))