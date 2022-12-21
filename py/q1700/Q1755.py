"""
 * 给你一个整数数组 nums 和一个目标值 goal 。
 * 你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum - goal) 。
 * 返回 abs(sum - goal) 可能的 最小值 。
 * 注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。
 * 提示：
 * 1、1 <= nums.length <= 40
 * 2、-10^7 <= nums[i] <= 10^7
 * 3、-10^9 <= goal <= 10^9
 * 链接：https://leetcode.cn/problems/closest-subsequence-sum/
"""
from typing import List


class Solution:

    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # n 的范围超过了30，不能直接使用二进制 dp，由于是40，可以考虑折半使用
        # 问题转换为，答案在l_sum或者r_sum中或者l_sum、r_sum中各一个
        n = len(nums)
        l_sum, r_sum = [0], [0]
        for i in range(n):
            sm = l_sum if i < n // 2 else r_sum
            for j in range(len(sm)):
                sm.append(sm[j] + nums[i])
        l_sum.sort()
        r_sum.sort()
        ans = abs(goal)
        for num in l_sum:  # 答案在 l_sum 中
            ans = min(ans, abs(goal - num))
        for num in r_sum:  # 答案在 r_sum 中
            ans = min(ans, abs(goal - num))
        # l_sum 和 r_sum 中各选一个，排序后双指针扫描
        i1, i2 = 0, len(r_sum) - 1
        while i1 < len(l_sum) and i2 >=0:
            s = l_sum[i1] + r_sum[i2]
            if s > goal:
                i2 -= 1
            else:
                i1 += 1
            ans = min(ans, abs(s-goal))
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().minAbsDifference([5, -7, 3, 5], 6))
    # 1
    print(Solution().minAbsDifference([7, -9, 15, -2], -5))
    # 7
    print(Solution().minAbsDifference([1, 2, 3], -7))
