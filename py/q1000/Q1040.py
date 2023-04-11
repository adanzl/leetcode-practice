"""
 * 在一个长度 无限 的数轴上，第 i 颗石子的位置为 stones[i]。如果一颗石子的位置最小/最大，那么该石子被称作 端点石子 。
 * 每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。
 * 值得注意的是，如果石子像 stones = [1,2,5] 这样，你将 无法 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。
 * 当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。
 * 要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves] 。
 * 提示：
 * 1、3 <= stones.length <= 10^4
 * 2、1 <= stones[i] <= 10^9
 * 3、stones[i] 的值各不相同。
 * 链接：https://leetcode.cn/problems/moving-stones-until-consecutive-ii/
"""
from typing import List


class Solution:

    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        mx = stones[n - 1] - stones[0] + 1 - n
        mx -= min(stones[n - 1] - stones[n - 2] - 1, stones[1] - stones[0] - 1)
        mn = mx
        j = 0
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1
            cost = n - (j - i + 1)
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            mn = min(mn, cost)

        return [mn, mx]


if __name__ == '__main__':
    # [2,3]
    print(Solution().numMovesStonesII([6, 5, 4, 3, 10]))
    # [1,2]
    print(Solution().numMovesStonesII([7, 4, 9]))
    # [0,0]
    print(Solution().numMovesStonesII([100, 101, 104, 102, 103]))
