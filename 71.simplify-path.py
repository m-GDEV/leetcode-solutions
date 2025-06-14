#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
from __future__ import annotations

# @lc code=start
class Folder:
    def __init__(self, name: str):
        self.name = name
        self.parent: 'Folder' = None
        # self.children: list[Folder] = []
        self.child: 'Folder' = None
    
    def append(self, node: 'Folder'):
        temp = self
        while temp.child != None:
            val = temp.child
            if val == None:
                break
            else:
                temp = val

        node.parent = temp 
        temp.child = node
    
    def pop(self):
        temp = self
        while temp.child != None:
            val = temp.child
            if val == None:
                break
            else:
                temp = val

        if temp.parent != None:
            temp.parent.child = None
        # need to remove the root (i.e. at root level /)
        else: 
            return True


class Solution:
    def simplifyPath(self, path: str) -> str:
        # for eg ''
        if len(path) < 1:
            self.error()
        # for eg 'home/'
        if path[0] != "/":
            self.error()
        # for eg '/'
        if len(path) == 1:
            return path
        # for eg '/home/./thing'
        while path.find('/./') != -1:
            path = path.replace("/./", "/")
        # for eg '/home//thing'
        path = path.replace("//", "/")
        # for eg '/home/'
        if path[-1] == "/":
            path = path[:-1]

        root = None
        ptr = None
        iterate = path.split("/")
        iterate = [item for item in iterate if item != '']

        for item in iterate:
            if item == ".":
                continue
            if item == "..":
                if root is not None:
                    r = root.pop()
                    if r == True:
                        root = None
                continue

            if root is None:
                root = Folder(item)
                ptr = root
            else:
                ptr = Folder(item)
                root.append(ptr)


        res = ""
        head = root 
        while head != None:
            res += f"/{head.name}"
            head = head.child


        if res == "":
            res = "/"

        print(res) 
        return res

def tryGet(s, pos):
    try:
        return s[pos]
    except:
        return None

def error(self):
    raise Exception()
# @lc code=end
f = Solution()
# f.simplifyPath("/home/")
# f.simplifyPath("/home//foo/")
# f.simplifyPath("/home/user/Documents/../Pictures")
# f.simplifyPath("/../")
# f.simplifyPath("/.../a/../b/c/../d/./")
# f.simplifyPath("/a/./b/../../c/")
# f.simplifyPath("/a//b////c/d//././/..")
f.simplifyPath("/.")
