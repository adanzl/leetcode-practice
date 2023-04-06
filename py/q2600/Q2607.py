"""
 * 给你一个下标从 0 开始的整数数组 arr 和一个整数 k 。数组 arr 是一个循环数组。
 * 换句话说，数组中的最后一个元素的下一个元素是数组中的第一个元素，数组中第一个元素的前一个元素是数组中的最后一个元素。
 * 你可以执行下述运算任意次：
 * 选中 arr 中任意一个元素，并使其值加上 1 或减去 1 。
 * 执行运算使每个长度为 k 的 子数组 的元素总和都相等，返回所需要的最少运算次数。
 * 子数组 是数组的一个连续部分。
 * 提示：
 * 1、1 <= k <= arr.length <= 10^5
 * 2、1 <= arr[i] <= 10^9
 * 链接：https://leetcode.cn/problems/make-k-subarray-sums-equal/
"""
from itertools import accumulate
from typing import List


class Solution:

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 0
        parent = [i for i in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def calc(arr):
            if not arr: return 0
            arr.sort()
            n = len(arr)
            pre_sum = [0] + list(accumulate(arr))
            vv = 10**15
            for i in range(n):
                vv = min(vv, arr[i] * (i + 1) - pre_sum[i + 1] + pre_sum[n] - pre_sum[i + 1] - arr[i] * (n - i - 1))
            return vv

        r = n % k
        for i in range(k):
            r1, r2 = find((i + r) % k), find(i)
            parent[r1] = r2

        r = [[] for _ in range(k)]
        for i in range(n):
            r[find(i % k)].append(arr[i])
        for a in r:
            ans += calc(a)

        return ans


if __name__ == '__main__':
    # 2
    print(Solution().makeSubKSumEqual([1, 4, 1, 3], k=2))
    # 5
    print(Solution().makeSubKSumEqual([2, 5, 5, 7], k=3))
