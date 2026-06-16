class Solution:
    def valid_sudoku(self,board):
        for row in range(0, 9):
            seen = set()
            for col in range(0, 9):
                value = board[row][col]
                if value == ".":
                    continue
                elif value in seen:
                    return False
                seen.add(value)

        for col in range(0, 9):
            seen = set()
            for row in range(0, 9):
                value = board[row][col]
                if value == ".":
                    continue
                elif value in seen:
                    return False
                seen.add(value)

        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                seen = set()
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        value = board[row][col]
                        if value == ".":
                            continue
                        elif value in seen:
                            return False
                        seen.add(value)
        return True
solution = Solution()
board = [
    ["5","2",".",".","3",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.valid_sudoku(board))

# Time complexity: O(n^4)
# Space complexity: O(n)