#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        import itertools
        elements = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        selected = list(digits)
        res = {}

        l = len(selected)
        if l == 1:
            return list(elements[int(digits)])
        elif l == 2:
            e1 = int(selected[0])
            e2 = int(selected[1])
            for i in range(len(elements[e1])):
                for j in range(len(elements[e2])):
                    f = (f"{elements[e1][i]}{elements[e2][j]}")
                    if res.get(f'{f}') == None:
                        res[f'{f}'] = f
        elif l == 3:
            e1 = int(selected[0])
            e2 = int(selected[1])
            e3 = int(selected[2])
            for i in range(len(elements[e1])):
                for j in range(len(elements[e2])):
                    for k in range(len(elements[e3])):
                        f = (f"{elements[e1][i]}{elements[e2][j]}{elements[e3][k]}")
                        if res.get(f'{f}') == None:
                            res[f'{f}'] = f
        elif l == 4:
            e1 = int(selected[0])
            e2 = int(selected[1])
            e3 = int(selected[2])
            e4 = int(selected[3])
            for i in range(len(elements[e1])):
                for j in range(len(elements[e2])):
                    for k in range(len(elements[e3])):
                        for l in range(len(elements[e4])):
                            f = (f"{elements[e1][i]}{elements[e2][j]}{elements[e3][k]}{elements[e4][l]}")
                            if res.get(f'{f}') == None:
                                res[f'{f}'] = f

        return list(res.values())

# @lc code=end
f = Solution()
s = f.letterCombinations("234")
pass