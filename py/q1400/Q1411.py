"""
 * 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
 * 给你网格图的行数 n 。
 * 请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
 * 提示：
 * 1、n == grid.length
 * 2、grid[i].length == 3
 * 3、1 <= n <= 5000
 * 链接：https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/
"""
from collections import defaultdict


class Solution:

    def numOfWays(self, n: int) -> int:
        if n == 1: return 12
        MOD = 10**9 + 7
        arr = ['121', '212', '312', '123', '213', '313', '131', '231', '321', '132', '232', '323']
        nx_list = defaultdict(list)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][0] != arr[j][0] and arr[i][1] != arr[j][1] and arr[i][2] != arr[j][2]:
                    nx_list[arr[i]].append(arr[j])
        dp = dict.fromkeys(arr, 1)
        for i in range(n - 1):
            ndp = defaultdict(int)
            for k, v in dp.items():
                for nx in nx_list[k]:
                    ndp[nx] += v
            dp = ndp
        return sum(dp.values()) % MOD


if __name__ == '__main__':
    # 12
    print(Solution().numOfWays(1))
    # 54
    print(Solution().numOfWays(2))
    # 106494
    print(Solution().numOfWays(7))
    # 30228214
    print(Solution().numOfWays(5000))