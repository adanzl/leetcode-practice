"""
 * 给出一个满足下述规则的二叉树：
 * 1、root.val == 0
 * 2、如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
 * 3、如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
 * 现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。
 * 请你先还原二叉树，然后实现 FindElements 类：
 * 1、FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
 * 2、bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。
 * 提示：
 * 1、TreeNode.val == -1
 * 2、二叉树的高度不超过 20
 * 3、节点的总数在 [1, 10^4] 之间
 * 4、调用 find() 的总次数在 [1, 10^4] 之间
 * 5、0 <= target <= 10^6
 * 链接：https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree
"""
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *
from typing import List

#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        if self.root is None: return False
        if target == 0: return True
        x = target + 1
        ln = x.bit_length()
        arr = []
        for i in range(ln - 1, -1, -1):
            arr.append((x - (1 << i)) & 1)
            x >>= 1
        p = self.root
        for i in arr[-2::-1]:
            nx = p.right if i else p.left
            if nx == None:
                return False
            p = nx
        return True

# @lc code=end

if __name__ == '__main__':
    obj = FindElements(stringToTreeNode('[-1,-1,-1,-1,-1]'))
    print(obj.find(5))  # False
    print(obj.find(1))  # True
    print(obj.find(2))  # True
    obj = FindElements(stringToTreeNode('[-1,null,-1]'))
    print(obj.find(2))  # True
    print(obj.find(1))  # False
    obj = FindElements(stringToTreeNode('[-1,null,-1,-1,null,-1]'))
    print(obj.find(2))  # True
    print(obj.find(3))  # False
    print(obj.find(4))  # False
    print(obj.find(5))  # True
