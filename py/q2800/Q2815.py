"""
 * 给你一个下标从 0 开始的整数数组 nums 。请你从 nums 中找出和 最大 的一对数，且这两个数数位上最大的数字相等。
 * 返回最大和，如果不存在满足题意的数字对，返回 -1 。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/max-pair-sum-in-an-array/
"""
from typing import List


class Solution:

    def maxSum(self, nums: List[int]) -> int:
        arr = [[] for _ in range(10)]
        ans = -1
        for num in nums:
            a = arr[int(max(str(num)))]
            for v in a:
                ans = max(ans, num + v)
            a.append(num)
        return ans


if __name__ == '__main__':
    # 88
    print(Solution().maxSum([51, 71, 17, 24, 42]))
    # -1
    print(Solution().maxSum([1, 2, 3, 4]))
