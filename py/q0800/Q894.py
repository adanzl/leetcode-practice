"""
 * 给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回。答案中每棵树的每个节点都必须符合 Node.val == 0 。
 * 答案的每个元素都是一棵真二叉树的根节点。你可以按 任意顺序 返回最终的真二叉树列表。
 * 真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点。
 * 提示：1 <= n <= 20
 * 链接：https://leetcode.cn/problems/all-possible-full-binary-trees/
"""
from typing import *
import copy, sys

sys.path.append(sys.path[0] + "/../")
from LCUtil import *


class Solution:

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []

        def func(n):
            if n == 1: return [TreeNode()]
            ans = []
            root = copy.deepcopy(TreeNode())
            n -= 1
            for i in range(1, n, 2):
                l, r = func(i), func(n - i)
                for rl in l:
                    for rr in r:
                        v = copy.deepcopy(root)
                        v.left = rl
                        v.right = rr
                        ans.append(v)
            return ans

        return func(n)


if __name__ == '__main__':
    # [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    print(treeNodeListToString(Solution().allPossibleFBT(7)))
    # [['0', '0', '0']]
    print(treeNodeListToString(Solution().allPossibleFBT(3)))
