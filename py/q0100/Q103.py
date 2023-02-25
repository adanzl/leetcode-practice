"""
 * 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
 * 提示：
 * 1、树中节点数目在范围 [0, 2000] 内
 * 2、-100 <= Node.val <= 100
 * 链接：https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
"""
from collections import deque
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        ans = []
        b = True
        while q:
            size = len(q)
            line = []
            for i in range(size):
                p = q.popleft()
                line.append(p.val)
                if p.left: q.append(p.left)
                if p.right: q.append(p.right)
            if b: ans.append(line)
            else: ans.append(line[::-1])
            b = not b
        return ans


if __name__ == '__main__':
    # [[3],[20,9],[15,7]]
    print(Solution().zigzagLevelOrder(stringToTreeNode("[3,9,20,null,null,15,7]")))
    # [[1]]
    print(Solution().zigzagLevelOrder(stringToTreeNode("[1]")))
    # []
    print(Solution().zigzagLevelOrder(stringToTreeNode("[]")))