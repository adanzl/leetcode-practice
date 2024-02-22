"""
 * 给定两个整数数组，pre_order 和 post_order ，其中 pre_order 是一个具有 无重复 值的二叉树的前序遍历，
 * post_order 是同一棵树的后序遍历，重构并返回二叉树。
 * 如果存在多个答案，您可以返回其中 任何 一个。
 * 提示：
 * 1、1 <= pre_order.length <= 30
 * 2、1 <= pre_order[i] <= pre_order.length
 * 3、pre_order 中所有值都 不同
 * 4、post_order.length == pre_order.length
 * 5、1 <= post_order[i] <= post_order.length
 * 6、post_order 中所有值都 不同
 * 7、保证 pre_order 和 post_order 是同一棵二叉树的前序遍历和后序遍历
 * 链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal
"""
from typing import List
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def constructFromPrePost(self, pre_order: List[int], post_order: List[int]) -> Optional[TreeNode]:

        def func(l_pre, r_pre, l_post, r_post):
            if l_pre == r_pre: return None
            root = TreeNode(pre_order[l_pre])
            for i in range(l_post, r_post - 1):
                if pre_order[l_pre + 1] == post_order[i]:
                    ln = i - l_post + 1
                    root.left = func(l_pre + 1, l_pre + 1 + ln, l_post, i + 1)
                    root.right = func(l_pre + 1 + ln, r_pre, i + 1, r_post - 1)
                    break
            return root

        return func(0, len(pre_order), 0, len(post_order))


if __name__ == '__main__':
    # [1,2,3,4,5,6,7]
    print(Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]))
    # [1]
    print(Solution().constructFromPrePost([1], [1]))
    #
    # print(Solution().constructFromPrePost())
