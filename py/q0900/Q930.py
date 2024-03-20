"""
 * 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
 * 子数组 是数组的一段连续部分。
 * 提示：
 * 1、1 <= nums.length <= 3 * 10^4
 * 2、nums[i] 不是 0 就是 1
 * 3、0 <= goal <= nums.length
 * 链接：https://leetcode.cn/problems/binary-subarrays-with-sum
"""
from typing import List


class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        cnt = {0: 1}
        sm = 0
        for num in nums:
            sm += num
            cnt[sm] = cnt.get(sm, 0) + 1
            if goal:
                ans += cnt.get(sm - goal, 0)
            else:
                ans += cnt.get(sm - goal, 0) - 1
        return ans


if __name__ == '__main__':
    # 15
    print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], goal=0))
    # 4
    print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], goal=2))
    #
    # print(Solution().numSubarraysWithSum())
