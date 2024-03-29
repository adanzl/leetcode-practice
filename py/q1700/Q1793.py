"""
 * 给你一个整数数组 nums （下标从 0 开始）和一个整数 k 。
 * 一个子数组 (i, j) 的 分数 定义为 min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1) 。
 * 一个 好 子数组的两个端点下标需要满足 i <= k <= j 。
 * 请你返回 好 子数组的最大可能 分数 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 2 * 10^4
 * 3、0 <= k < nums.length
 * 链接：https://leetcode.cn/problems/maximum-score-of-a-good-subarray/
"""
from typing import List


class Solution:

    def maximumScore1(self, nums: List[int], k: int) -> int:
        # 差分数组
        ans, n = 0, len(nums)
        LIMIT = max(nums) + 5
        diff_l, diff_r = [0] * LIMIT, [0] * LIMIT  # 差分
        pre_l, pre_r = nums[k], nums[k]
        for i in range(k, n):  # r
            v = min(pre_r, nums[i])  # 小于v的都+1
            diff_r[v + 1] -= 1
            diff_r[0] += 1
            pre_r = v
        for i in range(k, -1, -1):
            v = min(pre_l, nums[i])  # 小于v的都+1
            diff_l[v + 1] -= 1
            diff_l[0] += 1
            pre_l = v
        v_l, v_r = 0, 0
        for i in range(LIMIT):
            v_l += diff_l[i]
            v_r += diff_r[i]
            ans = max(ans, (v_l + v_r - 1) * i)
        return ans

    def maximumScore(self, nums: List[int], k: int) -> int:
        # 单调栈
        ans, n = 0, len(nums)
        s_l, s_r = [], []
        for i in range(k + 1):
            while s_l and nums[s_l[-1]] > nums[i]:
                s_l.pop()
            s_l.append(i)
        for i in range(n - 1, k - 1, -1):
            while s_r and nums[s_r[-1]] > nums[i]:
                s_r.pop()
            s_r.append(i)
        LIMIT = max(nums[s_l[-1]], nums[s_r[-1]])
        for v in range(LIMIT, 0, -1):
            i_l, i_r = -1, n
            while s_l and nums[s_l[-1]] >= v:
                s_l.pop()
            if s_l: i_l = s_l[-1]
            while s_r and nums[s_r[-1]] >= v:
                s_r.pop()
            if s_r: i_r = s_r[-1]
            ans = max(ans, (i_r - i_l - 1) * v)
        return ans


if __name__ == '__main__':
    # 15
    print(Solution().maximumScore([1, 4, 3, 7, 4, 5], 3))
    # 12
    print(Solution().maximumScore([7, 5, 4], 1))
    # 9732
    print(Solution().maximumScore([6569, 9667, 3148, 7698, 1622, 2194, 793, 9041, 1670, 1872], 5))
    # 20
    print(Solution().maximumScore([5, 5, 4, 5, 4, 1, 1, 1], 0))
