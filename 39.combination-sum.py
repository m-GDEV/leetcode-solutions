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
            # self.recurse(None, target, [candidates[i]], combs, False)
            self.root = BTreeNode(candidates[i])
            self.rec(self.root, target)
            print(self.root.__repr__())
            print("\n\nYASSS\n\n")

        return list(self.combs)


    def rec(self, root: BTreeNode, target):
        if self.getValFromLeaf(root) > target:
            return
        if self.getValFromLeaf(root) == target:
            l = sorted(self.getListFromLeaf(root))
            if self.combs.get(f'{l}') == None:
                self.combs[f'{l}'] = l
            return

        cans = self.candidates.copy()

        for i in range(len(cans)):
            leaf = BTreeNode(cans[i])
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

    def recurse2(self, cansog, target, currentList, combs, useCansOg):
        cans = self.candidates.copy()
        if useCansOg is True:
            cans = cansog.copy()

        if cans == [] and currentList == []:
            return
        elif cans == []:
            # cans = self.candidates.copy()
            currentList.pop()
            self.recurse(cansog, target, currentList, combs, True)
        elif sum(currentList) > target:
            del cans[0]
            currentList.pop()
            self.recurse(cansog, target, currentList, combs, True)
        elif sum(currentList) == target:
            combs.append(currentList.copy())
            del cans[0]
            currentList.pop()
            self.recurse(cansog, target, currentList, combs, True)
        else:
            currentList.append(cans[0])
            del cans[0]

            while cans != []:
                self.recurse(cans.copy(), target, currentList, combs, False) 


# @lc code=end
f = Solution()
# f.combinationSum([2,3,5], 8)
s = BTreeNode(5)
c = BTreeNode(6)
c.parent = s
c2 = BTreeNode(2)
c2.parent = c
c.children = [c2]
s.children = [c]

# f.getValFromLeaf(c2)
# f.combinationSum([2,3,6, 7], 7)
f.combinationSum([2,3,5], 8)