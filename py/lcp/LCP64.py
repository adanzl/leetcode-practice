"""
 * 「力扣嘉年华」的中心广场放置了一个巨型的二叉树形状的装饰树。每个节点上均有一盏灯和三个开关。
 * 节点值为 0 表示灯处于「关闭」状态，节点值为 1 表示灯处于「开启」状态。每个节点上的三个开关各自功能如下：
 * 1、开关 1：切换当前节点的灯的状态
 * 2、开关 2：切换 以当前节点为根 的子树中，所有节点上的灯的状态，
 * 3、开关 3：切换 当前节点及其左右子节点（若存在的话） 上的灯的状态
 * 给定该装饰的初始状态 root，请返回最少需要操作多少次开关，可以关闭所有节点的灯。
 * 提示：
 * 1、1 <= 节点个数 <= 10^5
 * 2、0 <= Node.val <= 1
 * 链接：https://leetcode.cn/problems/U7WvvU/
"""
from typing import *
import sys

sys.path.append(sys.path[0] + "/../")
from LCUtil import *


class Solution:

    def closeLampInTree(self, root: TreeNode) -> int:

        def func(node):
            if not node: return [0, 0, 0, 0]
            l, r = func(node.left), func(node.right)
            all_off, all_on, off_on, on_off = l[0] + r[0], l[1] + r[1], l[2] + r[2], l[3] + r[3]
            if node.val == 0:
                return [
                    min(all_off, all_on + 2, off_on + 2, on_off + 2),
                    min(all_off + 1, all_on + 1, off_on + 1, on_off + 3),
                    min(all_off + 2, all_on, off_on + 2, on_off + 2),
                    min(all_off + 1, all_on + 1, off_on + 3, on_off + 1),
                ]
            else:
                return [
                    min(all_off + 1, all_on + 1, off_on + 3, on_off + 1),
                    min(all_off + 2, all_on, off_on + 2, on_off + 2),
                    min(all_off + 1, all_on + 1, off_on + 1, on_off + 3),
                    min(all_off, all_on + 2, off_on + 2, on_off + 2),
                ]

        return func(root)[0]


if __name__ == '__main__':
    # 2
    print(Solution().closeLampInTree(stringToTreeNode("[1,1,0,null,null,null,1]")))
    # 1
    print(Solution().closeLampInTree(stringToTreeNode("[1,1,1,1,null,null,1]")))
    # 0
    print(Solution().closeLampInTree(stringToTreeNode("[0,null,0]")))