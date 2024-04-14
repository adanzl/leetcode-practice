"""
 * 给你一个 正 整数数组 nums 。
 * 请你求出 nums 中有多少个子数组，满足子数组中 第一个 和 最后一个 元素都是这个子数组中的 最大 值。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
"""
from typing import List


class Solution:

    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = 0
        q = []
        for num in nums:
            while q and q[-1][0] < num:
                q.pop()
            if q and q[-1][0] == num:
                q[-1][1] += 1
                ans += q[-1][1]
            else:
                q.append([num, 1])
                ans += 1
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().numberOfSubarrays([1, 4, 3, 3, 2]))
    # 6
    print(Solution().numberOfSubarrays([3, 3, 3]))
    # 1
    print(Solution().numberOfSubarrays([1]))
