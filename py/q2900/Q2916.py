"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 定义 nums 一个子数组的 不同计数 值如下：
 * 令 nums[i..j] 表示 nums 中所有下标在 i 到 j 范围内的元素构成的子数组（满足 0 <= i <= j < nums.length ），
 * 那么我们称子数组 nums[i..j] 中不同值的数目为 nums[i..j] 的不同计数。
 * 请你返回 nums 中所有子数组的 不同计数 的 平方 和。
 * 由于答案可能会很大，请你将它对 10^9 + 7 取余 后返回。
 * 子数组指的是一个数组里面一段连续 非空 的元素序列。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-ii/
"""

from collections import defaultdict
from typing import List

#
# @lc app=leetcode.cn id=2916 lang=python3
#
# [2916] 子数组不同元素数目的平方和 II
#


# @lc code=start
class Solution:

    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        # tree 表示求和
        tree = [0 for _ in range(2 << n.bit_length())]
        # 值可能为0时，dirty设置为-1
        dirty = [-1 for _ in range(2 << n.bit_length())]

        def push_down(o, l, r):
            if dirty[o] == -1: return
            mid = (l + r) >> 1
            set_value(o * 2 + 1, l, mid, l, mid, dirty[o])
            set_value(o * 2 + 2, mid + 1, r, mid + 1, r, dirty[o])
            dirty[o] = -1

        def set_value(o, l, r, L, R, val):
            # o: 根节点 l：区间左端点 r：区间右端点 LR：更新下标范围 val：更新值
            mid = (l + r) >> 1
            if l == L and r == R:
                tree[o] += val * (r - l + 1)
                if dirty[o] != -1:
                    dirty[o] += val
                else:
                    dirty[o] = val
                return
            push_down(o, l, r)
            if R <= mid:
                set_value(o * 2 + 1, l, mid, L, R, val)
            elif mid + 1 <= L:
                set_value(o * 2 + 2, mid + 1, r, L, R, val)
            else:
                set_value(o * 2 + 1, l, mid, L, mid, val)
                set_value(o * 2 + 2, mid + 1, r, mid + 1, R, val)
            process(o, l, r)

        def query(o, l, r, L, R):
            if l == L and r == R:
                return tree[o]
            push_down(o, l, r)
            mid = (l + r) >> 1
            if R <= mid:
                return query(o * 2 + 1, l, mid, L, R)
            if mid + 1 <= L:
                return query(o * 2 + 2, mid + 1, r, L, R)
            return query(o * 2 + 1, l, mid, L, mid) + query(o * 2 + 2, mid + 1, r, mid + 1, R)

        def process(o, l, r):
            if l == r: return
            a, b = tree[o * 2 + 1], tree[o * 2 + 2]
            tree[o] = a + b

        ans, pre = 0, 0
        lst = defaultdict(lambda: -1)
        for i, num in enumerate(nums):
            ii = lst[num]
            pre += (2 * query(0, 0, n - 1, ii + 1, i) + i - ii) % MOD
            set_value(0, 0, n - 1, ii + 1, i, 1)
            ans = (ans + pre) % MOD
            lst[num] = i
        return ans


# @lc code=end

if __name__ == '__main__':
    # 578
    print(Solution().sumCounts([5, 2, 4, 2, 1, 3, 2, 4, 3, 1]))
    # 15
    print(Solution().sumCounts([1, 2, 1]))
    # 3
    print(Solution().sumCounts([2, 2]))
