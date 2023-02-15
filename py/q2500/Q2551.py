"""
 * 你有 k 个背包。给你一个下标从 0 开始的整数数组 weights ，其中 weights[i] 是第 i 个珠子的重量。同时给你整数 k 。
 * 请你按照如下规则将所有的珠子放进 k 个背包。
 * 1、没有背包是空的。
 * 2、如果第 i 个珠子和第 j 个珠子在同一个背包里，那么下标在 i 到 j 之间的所有珠子都必须在这同一个背包中。
 * 3、如果一个背包有下标从 i 到 j 的所有珠子，那么这个背包的价格是 weights[i] + weights[j] 。
 * 一个珠子分配方案的 分数 是所有 k 个背包的价格之和。
 * 请你返回所有分配方案中，最大分数 与 最小分数 的 差值 为多少。
 * 提示：
 * 1、1 <= k <= weights.length <= 10^5
 * 2、1 <= weights[i] <= 10^9
 * 链接：https://leetcode.cn/problems/put-marbles-in-bags/
"""
from itertools import pairwise
from typing import List


class Solution:

    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = sorted([abs(a + b) for a, b in pairwise(weights)])
        ans, n = 0, len(arr)
        for i in range(k - 1):
            ans += arr[n - 1 - i] - arr[i]
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().putMarbles([1, 3, 5, 1], k=2))
    # 0
    print(Solution().putMarbles([1, 3], k=2))
