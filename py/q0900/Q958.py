"""
 * 给定一个二叉树的 root ，确定它是否是一个 完全二叉树 。
 * 在一个 完全二叉树 中，除了最后一个关卡外，所有关卡都是完全被填满的，并且最后一个关卡中的所有节点都是尽可能靠左的。它可以包含 1 到 2h 节点之间的最后一级 h 。
 * 提示：
 * 1、树的结点数在范围  [1, 100] 内。
 * 2、1 <= Node.val <= 1000
 * 链接：https://leetcode.cn/problems/check-completeness-of-a-binary-tree/
"""

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = [root]
        end = False
        while q and not end:
            t = q
            q = []
            for node in t:
                if end and (node.left or node.right):
                    return False
                if node.left:
                    q.append(node.left)
                else:
                    if node.right:
                        return False
                if node.right:
                    q.append(node.right)
                else:
                    end = True
        return all(not node.left and not node.right for node in q)


if __name__ == '__main__':
    # False
    print(Solution().isCompleteTree(stringToTreeNode("[1,2,3,5,null,7,8]")))
    # True
    print(Solution().isCompleteTree(stringToTreeNode("[1,2,3,4,5,6]")))
    # False
    print(Solution().isCompleteTree(stringToTreeNode("[1,2,3,4,5,null,7]")))