"""
 * Bob 站在单元格 (0, 0) ，想要前往目的地 destination ：(row, column) 。他只能向 右 或向 下 走。你可以为 Bob 提供导航 指令 来帮助他到达目的地 destination 。
 * 指令 用字符串表示，其中每个字符：
 * 1、'H' ，意味着水平向右移动
 * 2、'V' ，意味着竖直向下移动
 * 能够为 Bob 导航到目的地 destination 的指令可以有多种，例如，如果目的地 destination 是 (2, 3)，"HHHVV" 和 "HVHVH" 都是有效 指令 。
 * 然而，Bob 很挑剔。因为他的幸运数字是 k，他想要遵循 按字典序排列后的第 k 条最小指令 的导航前往目的地 destination 。k  的编号 从 1 开始 。
 * 给你一个整数数组 destination 和一个整数 k ，请你返回可以为 Bob 提供前往目的地 destination 导航的 按字典序排列后的第 k 条最小指令 。
 * 提示：
 * 1、destination.length == 2
 * 2、1 <= row, column <= 15
 * 3、1 <= k <= nCr(row + column, row)，其中 nCr(a, b) 表示组合数，即从 a 个物品中选 b 个物品的不同方案数。
 * 链接：https://leetcode.cn/problems/kth-smallest-instructions/
"""
from math import comb
from typing import List


class Solution:

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        ans = []
        for _ in range(h + v):
            if h <= 0: break
            o = comb(h + v - 1, h - 1)  # ans[i] = 'H'
            if k > o:
                ans.append("V")
                v -= 1
                k -= o
            else:
                ans.append("H")
                h -= 1
        ans.extend(["V"] * v)
        return "".join(ans)


if __name__ == '__main__':
    # VVVVVVVVVVVVVVVHHHHHHHHHHHHHHH
    print(Solution().kthSmallestPath([15, 15], 155117520))
    # "HHVHV"
    print(Solution().kthSmallestPath([2, 3], 2))
    # "HHHVV"
    print(Solution().kthSmallestPath([2, 3], 1))
    # "HHVVH"
    print(Solution().kthSmallestPath([2, 3], 3))