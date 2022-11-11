"""
 * 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
 * 二叉搜索树的定义如下：
 * 1、任意节点的左子树中的键值都 小于 此节点的键值。
 * 2、任意节点的右子树中的键值都 大于 此节点的键值。
 * 3、任意节点的左子树和右子树都是二叉搜索树。
 * 提示：
 * 1、每棵树有 1 到 40000 个节点。
 * 2、每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
 * 链接：https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/
"""
import os
import sys

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            if root is None: return True, None, None, 0
            nonlocal ans
            b_l, mx_l, mn_l, v_l = dfs(root.left)
            b_r, mx_r, mn_r, v_r = dfs(root.right)
            b = b_l and b_r and (mx_l is None or mx_l < root.val) and (mn_r is None or root.val < mn_r)
            val = v_l + v_r + root.val
            if b: ans = max(ans, val)
            mx = root.val if mx_r is None else mx_r
            mn = root.val if mn_l is None else mn_l
            return b, mx, mn, val

        dfs(root)
        return ans


if __name__ == '__main__':
    # 20
    print(Solution().maxSumBST(stringToTreeNode("[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]")))
    # 2
    print(Solution().maxSumBST(stringToTreeNode("[4,3,null,1,2]")))
    # 0
    print(Solution().maxSumBST(stringToTreeNode("[-4,-2,-5]")))
    # 6
    print(Solution().maxSumBST(stringToTreeNode("[2,1,3]")))
    # 7
    print(Solution().maxSumBST(stringToTreeNode("[5,4,8,3,null,6,3]")))