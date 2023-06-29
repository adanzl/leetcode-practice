"""
 * 给你一个下标从 0 开始大小为 m x n 的二进制矩阵 grid 。
 * 从原矩阵中选出若干行构成一个行的 非空 子集，如果子集中任何一列的和至多为子集大小的一半，那么我们称这个子集是 好子集。
 * 更正式的，如果选出来的行子集大小（即行的数量）为 k，那么每一列的和至多为 floor(k / 2) 。
 * 请你返回一个整数数组，它包含好子集的行下标，请你将子集中的元素 升序 返回。
 * 如果有多个好子集，你可以返回任意一个。如果没有好子集，请你返回一个空数组。
 * 一个矩阵 grid 的行 子集 ，是删除 grid 中某些（也可能不删除）行后，剩余行构成的元素集合。
 * 提示：
 * 1、m == grid.length
 * 2、n == grid[i].length
 * 3、1 <= m <= 10^4
 * 4、1 <= n <= 5
 * 5、grid[i][j] 要么是 0 ，要么是 1 。
 * 链接：https://leetcode.cn/problems/find-a-good-subset-of-the-matrix/
"""
from collections import defaultdict
from typing import List


class Solution:

    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        states = defaultdict(list)
        for i in range(m):
            tmp = 0
            for j in range(n):
                tmp = tmp * 2 + grid[i][j]

            states[tmp].append(i)

        # 贪心，开选
        res = []
        if states[0]:
            return states[0]

        tgt = 1 << n
        ss = tgt - 1

        # 枚举第一行
        for lstate in range(tgt):
            if not states[lstate]:
                continue

            # 补集
            rstate = ss ^ lstate

            s = rstate
            # 获取补集的所有子集
            while s:
                if states[s]:
                    res = [states[lstate][0], states[s][0]]
                    res.sort()
                    return res
                s = (s - 1) & rstate
        return []


if __name__ == '__main__':
    # [0,1]
    print(Solution().goodSubsetofBinaryMatrix([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]))
    # [0]
    print(Solution().goodSubsetofBinaryMatrix([[0]]))
    # []
    print(Solution().goodSubsetofBinaryMatrix([[1, 1, 1], [1, 1, 1]]))
