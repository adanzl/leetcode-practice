"""
 * 给你一个 二维 整数数组 coordinates 和一个整数 k ，其中 coordinates[i] = [xi, yi] 是第 i 个点在二维平面里的坐标。
 * 我们定义两个点 (x1, y1) 和 (x2, y2) 的 距离 为 (x1 XOR x2) + (y1 XOR y2) ，XOR 指的是按位异或运算。
 * 请你返回满足 i < j 且点 i 和点 j之间距离为 k 的点对数目。
 * 提示：
 * 1、2 <= coordinates.length <= 5 * 10^4
 * 2、0 <= xi, yi <= 10^6
 * 3、0 <= k <= 100
 * 链接：https://leetcode.cn/problems/count-pairs-of-points-with-distance-k/
"""
from collections import Counter
from typing import List


class Solution:

    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        mem = Counter()
        ans = 0
        for i in range(n):
            xi, yi = coordinates[i]
            for v1 in range(0, k + 1):
                ox, oy = v1 ^ xi, (k - v1) ^ yi
                ans += mem[(ox, oy)]
            mem[(xi, yi)] += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().countPairs([[1, 2], [4, 2], [1, 3], [5, 2]], k=5))
    # 10
    print(Solution().countPairs([[1, 3], [1, 3], [1, 3], [1, 3], [1, 3]], k=0))