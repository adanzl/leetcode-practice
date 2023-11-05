"""
 * 给你一个由 不同 整数组成的整数数组 arr 和一个整数 k 。
 * 每回合游戏都在数组的前两个元素（即 arr[0] 和 arr[1] ）之间进行。
 * 比较 arr[0] 与 arr[1] 的大小，较大的整数将会取得这一回合的胜利并保留在位置 0 ，较小的整数移至数组的末尾。
 * 当一个整数赢得 k 个连续回合时，游戏结束，该整数就是比赛的 赢家 。
 * 返回赢得比赛的整数。
 * 题目数据 保证 游戏存在赢家。
 * 提示：
 * 1、2 <= arr.length <= 10^5
 * 2、1 <= arr[i] <= 10^6
 * 3、arr 所含的整数 各不相同 。
 * 4、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-winner-of-an-array-game
"""
from typing import List


class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k > n: return max(arr)
        mx, mx_i = arr[0], 0
        for i in range(1, n * 2):
            if arr[i % n] < mx:
                if (i - mx_i >= k - 1 and mx_i > 0) or i - mx_i >= k:
                    return mx
            else:
                mx, mx_i = arr[i], i
                if k == 1: return mx
        return 0


if __name__ == '__main__':
    # 25
    print(Solution().getWinner([1, 25, 35, 42, 68, 70], k=1))
    # 5
    print(Solution().getWinner([2, 1, 3, 5, 4, 6, 7], k=2))
    # 3
    print(Solution().getWinner([3, 2, 1], k=10))
    # 9
    print(Solution().getWinner([1, 9, 8, 2, 3, 7, 6, 4, 5], k=7))
    # 99
    print(Solution().getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], k=1000000000))
