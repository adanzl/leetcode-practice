"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * nums 一个长度为 k 的 子序列 指的是选出 k 个 下标 i_0 < i_1 < ... < i_k-1 ，如果这个子序列满足以下条件，我们说它是 平衡的 ：
 * 对于范围 [1, k - 1] 内的所有 j ，nums[i_j] - nums[i_j-1] >= i_j - i_j-1 都成立。
 * nums 长度为 1 的 子序列 是平衡的。
 * 请你返回一个整数，表示 nums 平衡 子序列里面的 最大元素和 。
 * 一个数组的 子序列 指的是从原数组中删除一些元素（也可能一个元素也不删除）后，剩余元素保持相对顺序得到的 非空 新数组。
 * 提示：
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-balanced-subsequence-sum/
"""
from bisect import bisect_left
from typing import List

inf = 10**30


class Solution:

    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        b = sorted(set(x - i for i, x in enumerate(nums)))  # 离散化 nums[i]-i
        t = BIT(len(b) + 1)
        ans = -inf
        for i, x in enumerate(nums):
            j = bisect_left(b, x - i) + 1  # nums[i]-i 离散化后的值（从 1 开始）
            f = max(t.pre_max(j), 0) + x
            ans = max(ans, f)
            t.update(j, f)
        return ans


# 树状数组模板（维护前缀最大值）
class BIT:

    def __init__(self, n: int):
        self.tree = [-inf] * n

    def update(self, i: int, val: int) -> None:
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & -i

    def pre_max(self, i: int) -> int:
        mx = -inf
        while i > 0:
            mx = max(mx, self.tree[i])
            i &= i - 1
        return mx


if __name__ == '__main__':
    # 14
    print(Solution().maxBalancedSubsequenceSum([3, 3, 5, 6]))
    # 13
    print(Solution().maxBalancedSubsequenceSum([5, -1, -3, 8]))
    # -1
    print(Solution().maxBalancedSubsequenceSum([-2, -1]))
