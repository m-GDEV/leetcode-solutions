#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row check
        for row in board:
            nums = {}
            for item in row:
                if item == ".":
                    continue
                if nums.get(item) == None:
                    nums[item] = 1
                else:
                    return False
        # column check
        for i in range(len(board)):
            nums = {}
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if nums.get(board[j][i]) == None:
                    nums[board[j][i]] = 1
                else:
                    return False
       # box check 
        box_pos = [0, 3, 6]
        for x in box_pos:
            for y in box_pos:
                # explore this box
                nums = {}
                for i in range(x, x+3):
                    for k in range(y, y+3):
                        if board[i][k] == ".":
                            continue
                        if nums.get(board[i][k]) == None:
                            nums[board[i][k]] = 1
                        else:
                            return False

        return True
# @lc code=end

f = Solution()
# k = f.isValidSudoku([["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]])
k = f.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(k)