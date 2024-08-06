"""
 * 给你一个整数数组 nums 和一个二维数组 queries，其中 queries[i] = [pos_i, x_i]。
 * 对于每个查询 i，首先将 nums[pos_i] 设置为 x_i，然后计算查询 i 的答案，该答案为 nums 中 不包含相邻元素 的 子序列 的 最大 和。
 * 返回所有查询的答案之和。
 * 由于最终答案可能非常大，返回其对 10^9 + 7 取余 的结果。
 * 子序列 是指从另一个数组中删除一些或不删除元素而不改变剩余元素顺序得到的数组。
 * 提示：
 * 1、1 <= nums.length <= 5 * 10^4
 * 2、-10^5 <= nums[i] <= 10^5
 * 3、1 <= queries.length <= 5 * 10^4
 * 4、queries[i] == [pos_i, x_i]
 * 5、0 <= pos_i <= nums.length - 1
 * 6、-10^5 <= x_i <= 10^5
 * 链接：https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
"""

from typing import List

#
# @lc app=leetcode.cn id=3165 lang=python3
#
# [3165] 不包含相邻元素的子序列的最大和
#

# @lc code=start


class Solution:

    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        # 两边都不取             tree[o][00] = max(a[01]+b[00], a[00]+b[10])
        # 左边不取，右边可取可不取 tree[o][01] = max(a[01]+b[01], a[00]+b[11])
        # 左边可取可不取，右边不取 tree[o][10] = max(a[11]+b[00], a[10]+b[10])
        # 两边都可取可不取        tree[o][11] = max(a[11]+b[01], a[10]+b[11])
        tree = [[0] * 4 for _ in range(2 << n.bit_length())]

        # 单点更新线段树，不需要查询，可以分治、并且需要局部更新的结构可以使用线段树
        def set_value(o, l, r, idx, val):
            # o: 根节点；l：区间左端点；r：区间右端点；idx：更新下标；val：更新值
            mid = (l + r) >> 1
            if l == idx and r == idx:
                tree[o][3] = max(val, 0)
                return
            if idx <= mid:
                set_value(o * 2 + 1, l, mid, idx, val)
            else:
                set_value(o * 2 + 2, mid + 1, r, idx, val)
            process(o)

        def process(o):
            a, b = tree[o * 2 + 1], tree[o * 2 + 2]
            tree[o][0] = max(a[1] + b[0], a[0] + b[2])
            tree[o][1] = max(a[1] + b[1], a[0] + b[3])
            tree[o][2] = max(a[3] + b[0], a[2] + b[2])
            tree[o][3] = max(a[3] + b[1], a[2] + b[3])

        for i, num in enumerate(nums):
            set_value(0, 0, n - 1, i, num)
        ans = 0
        for idx, num in queries:
            set_value(0, 0, n - 1, idx, num)
            ans += tree[0][3]
        return ans % MOD


# @lc code=end

if __name__ == '__main__':
    # 36
    print(Solution().maximumSumSubsequence([4, 0, -1, -2, 3, 1, -1],
                                           [[3, 1], [0, -2], [1, -1], [0, -2], [5, 4], [6, -3], [6, -2], [2, -1]]))
    # 21
    print(Solution().maximumSumSubsequence([3, 5, 9], queries=[[1, -2], [0, -3]]))
    # 0
    print(Solution().maximumSumSubsequence([0, -1], queries=[[0, -5]]))
