"""
 * 给你一个由非负整数组成的数组 nums 。
 * 另有一个查询数组 queries ，其中 queries[i] = [x_i, m_i] 。
 * 第 i 个查询的答案是 x_i 和任何 nums 数组中不超过 m_i 的元素按位异或（XOR）得到的最大值。
 * 换句话说，答案是 max(nums[j] XOR x_i) ，其中所有 j 均满足 nums[j] <= m_i 。
 * 如果 nums 中的所有元素都大于 m_i，最终答案就是 -1 。
 * 返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个查询的答案。
 * 提示：
 * 1、1 <= nums.length, queries.length <= 10^5
 * 2、queries[i].length == 2
 * 3、0 <= nums[j], x_i, m_i <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-xor-with-an-element-from-array
"""

from typing import List

#
# @lc app=leetcode.cn id=1707 lang=python3
#
# [1707] 与数组中元素的最大异或值
#


# @lc code=start
class Solution:

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, idx = len(queries), 0
        ans = [-1] * n
        nums.sort()
        t = [[], []]

        def add_num(t, num, ii):
            if ii < 0: return
            sub = t[int(bool(num & (1 << ii)))]
            if len(sub) == 0:
                sub.append([])
                sub.append([])
            add_num(sub, num, ii - 1)

        def query(t, x, ii):
            if ii < 0: return 0
            f = int(bool(x & 1 << ii))  # 当前位
            sub = t[f ^ 1]  # 当前位是0则选1，否则选0
            ret = 1 << ii
            if len(sub) == 0:
                sub = t[f]
                ret = 0
            return ret + query(sub, x, ii - 1)

        qq = sorted([[m, x, i] for i, (x, m) in enumerate(queries)])
        for m, x, i in qq:
            while idx < len(nums) and nums[idx] <= m:
                add_num(t, nums[idx], 32)
                idx += 1
            if t[0] or t[1]:
                ans[i] = query(t, x, 32)
        return ans


# @lc code=end

if __name__ == '__main__':
    # [15,-1,5]
    print(Solution().maximizeXor([5, 2, 4, 6, 6, 3], queries=[[12, 4], [8, 1], [6, 3]]))
    # [3,3,7]
    print(Solution().maximizeXor([0, 1, 2, 3, 4], queries=[[3, 1], [1, 3], [5, 6]]))
