"""
 * 给你一棵 完美 二叉树的根节点 root ，请你反转这棵树中每个 奇数 层的节点值。
 * 例如，假设第 3 层的节点值是 [2,1,3,4,7,11,29,18] ，那么反转后它应该变成 [18,29,11,7,4,3,1,2] 。
 * 反转后，返回树的根节点。
 * 完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。
 * 节点的 层数 等于该节点到根节点之间的边数。
 * 提示：
 * 1、树中的节点数目在范围 [1, 2^14] 内
 * 2、0 <= Node.val <= 105
 * 3、root 是一棵 完美 二叉树
 * 链接：https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/
"""

from typing import *
from collections import *

import sys
sys.path.append(sys.path[0] + "/../")
from LCUtil import *


class Solution:

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        deep = 0
        while q:
            size = len(q)
            line = []
            for _ in range(size):
                cur = q.popleft()
                if deep % 2 == 1:
                    line.append(cur)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            for i in range(int(len(line) / 2)):
                line[len(line) - i - 1].val, line[i].val = line[i].val, line[len(line) - i - 1].val
            deep += 1
        return root


if __name__ == '__main__':
    # [2,5,3,8,13,21,34]
    print(treeNodeToString(Solution().reverseOddLevels(stringToTreeNode("[2,3,5,8,13,21,34]"))))
    # [7,11,13]
    print(treeNodeToString(Solution().reverseOddLevels(stringToTreeNode("[7,13,11]"))))
    # [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
    print(treeNodeToString(Solution().reverseOddLevels(stringToTreeNode("[0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]"))))