"""
 * 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个 [0, 25] 范围内的值，分别代表字母 'a' 到 'z'。
 * 返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
 * 注：字符串中任何较短的前缀在 字典序上 都是 较小 的：
 * 例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。 
 * 节点的叶节点是没有子节点的节点。
 * 提示：
 * 1、给定树的结点数在 [1, 8500] 范围内
 * 2、0 <= Node.val <= 25
 * 链接：https://leetcode.cn/problems/smallest-string-starting-from-leaf
"""

import copy
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *

#
# @lc app=leetcode.cn id=988 lang=python3
#
# [988] 从叶结点开始的最小字符串
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []

        def dfs(root, path):
            if root is None: return
            nonlocal ans
            path.appendleft(root.val)
            if root.left is None and root.right is None:
                for a, b in zip(ans, path):
                    if a == b: continue
                    if a > b:
                        ans = copy.copy(path)
                    path.popleft()
                    return
                if not ans or len(ans) > len(path):
                    ans = copy.copy(path)
                path.popleft()
                return
            dfs(root.left, path)
            dfs(root.right, path)
            path.popleft()

        dfs(root, Deque())
        return ''.join([chr(v + ord('a')) for v in ans])


# @lc code=end

if __name__ == '__main__':
    # "ba"
    print(Solution().smallestFromLeaf(stringToTreeNode('[0,null,1]')))
    # "abc"
    print(Solution().smallestFromLeaf(stringToTreeNode('[2,2,1,null,1,0,null,0]')))
    # "dba"
    print(Solution().smallestFromLeaf(stringToTreeNode('[0,1,2,3,4,3,4]')))
    # "adz"
    print(Solution().smallestFromLeaf(stringToTreeNode('[25,1,3,1,3,0,2]')))
