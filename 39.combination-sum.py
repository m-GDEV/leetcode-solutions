#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# @lc code=start
class BTreeNode:
    def __init__(self, val):
        self.val = val
        self.children: list[BTreeNode] = []
        self.parent = None

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.val)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.combs = {}
        self.candidates = candidates

        for i in range(len(candidates)):
            self.root = BTreeNode(candidates[i])
            self.rec(self.root, target)

        return list(self.combs.values())


    def rec(self, root: BTreeNode, target):
        if self.getValFromLeaf(root) > target:
            return
        if self.getValFromLeaf(root) == target:
            l = sorted(self.getListFromLeaf(root))
            if self.combs.get(f'{l}') == None:
                self.combs[f'{l}'] = l
            return

        for i in range(len(self.candidates)):
            leaf = BTreeNode(self.candidates[i])
            leaf.parent = root
            root.children.append(leaf)

            self.rec(leaf, target)

    def getValFromLeaf(self, node: BTreeNode):
        return sum(self.getListFromLeaf(node))

    def getListFromLeaf(self, node: BTreeNode):
        val = []
        while node != None: 
            val.append(node.val)
            node = node.parent
        
        return val


# @lc code=end
f = Solution()
f.combinationSum([2,3,5], 8)

# f.combinationSum([2,3,5], 8)
# s = BTreeNode(5)
# c = BTreeNode(6)
# c.parent = s
# c2 = BTreeNode(2)
# c2.parent = c
# c.children = [c2]
# s.children = [c]

# f.getValFromLeaf(c2)
# f.combinationSum([2,3,6, 7], 7)