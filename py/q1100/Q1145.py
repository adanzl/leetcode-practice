"""
 * 有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。
 * 最开始时：
 * 1、「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）
 * 2、「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。
 * 3、「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。
 * 之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。
 * 如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。
 * 若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。
 * 现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true ；若无法获胜，就请返回 false 。
 * 提示：
 * 1、树中节点数目为 n
 * 2、1 <= x <= n <= 100
 * 3、n 是奇数
 * 4、1 <= Node.val <= n
 * 5、树中所有值 互不相同
 * 链接：https://leetcode.cn/problems/binary-tree-coloring-game/
"""
from typing import Optional
import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        if root is None: return False
        pa, sub = [0] * (n + 1), [0] * (n + 1)
        cnt_left, cnt_right = 0, 0

        def dfs(root: Optional[TreeNode], parent: int):
            if root is None:
                return 0
            pa[root.val] = parent
            l = dfs(root.left, root.val)
            r = dfs(root.right, root.val)
            sub[root.val] = l + r + 1
            nonlocal cnt_left, cnt_right
            if root.val == x:
                cnt_left = l
                cnt_right = r
            return sub[root.val]

        dfs(root, 0)
        # pa, left, right
        cnt_pa = sub[root.val] - sub[x]
        return cnt_pa > sub[x] or cnt_left > sub[root.val] - cnt_left or cnt_right > sub[root.val] - cnt_right


if __name__ == '__main__':
    # False
    print(Solution().btreeGameWinningMove(stringToTreeNode("[5,null,4,2,null,3,1]"), n=5, x=2))
    # True
    print(Solution().btreeGameWinningMove(stringToTreeNode("[1,2,3,4,5,6,7,8,9,10,11]"), n=11, x=3))
    # False
    print(Solution().btreeGameWinningMove(stringToTreeNode("[1,2,3]"), n=3, x=1))
