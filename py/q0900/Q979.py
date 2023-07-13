"""
 * 给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。
 * 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。
 * (移动可以是从父结点到子结点，或者从子结点移动到父结点。)。
 * 返回使每个结点上只有一枚硬币所需的移动次数。
 * 提示：
 * 1、1<= N <= 100
 * 2、0 <= node.val <= N
 * 链接：https://leetcode.cn/problems/distribute-coins-in-binary-tree/
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            ans += abs(l) + abs(r)
            return node.val + l + r - 1

        dfs(root)
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().distributeCoins(stringToTreeNode("[3,0,0]")))
    # 3
    print(Solution().distributeCoins(stringToTreeNode("[0,3,0]")))
    # 2
    print(Solution().distributeCoins(stringToTreeNode("[1,0,2]")))
    # 4
    print(Solution().distributeCoins(stringToTreeNode("[1,0,0,null,3]")))