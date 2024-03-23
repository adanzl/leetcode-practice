"""
 * 给你一个长度为 n 的数组 nums 和一个 正 整数 k 。
 * 如果 nums 的一个子数组中，第一个元素和最后一个元素 差的绝对值恰好 为 k ，我们称这个子数组为 好 的。
 * 换句话说，如果子数组 nums[i..j] 满足 |nums[i] - nums[j]| == k ，那么它是一个好子数组。
 * 请你返回 nums 中 好 子数组的 最大 和，如果没有好子数组，返回 0 。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、-10^9 <= nums[i] <= 10^9
 * 3、1 <= k <= 10^9
 * 链接：https://leetcode.cn/problems/maximum-good-subarray-sum/
"""
from typing import List


class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        p_sum_dic = {}
        MN = -10**20
        sm = 0
        ans = MN
        for i, num in enumerate(nums):
            if num - k in p_sum_dic:
                ans = max(ans, sm + num - p_sum_dic[num - k])
            if num + k in p_sum_dic:
                ans = max(ans, sm + num - p_sum_dic[num + k])
            if num in p_sum_dic:
                p_sum_dic[num] = min(p_sum_dic[num], sm)
            else:
                p_sum_dic[num] = sm
            sm += num
        return ans if ans != MN else 0


if __name__ == '__main__':
    # 8
    print(Solution().maximumSubarraySum([3, 3, 2], 1))
    # 11
    print(Solution().maximumSubarraySum([1, 2, 3, 4, 5, 6], k=1))
    # 11
    print(Solution().maximumSubarraySum([-1, 3, 2, 4, 5], k=3))
    # -6
    print(Solution().maximumSubarraySum([-1, -2, -3, -4], k=2))
