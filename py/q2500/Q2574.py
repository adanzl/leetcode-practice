"""
 * 给你一个下标从 0 开始的整数数组 nums ，请你找出一个下标从 0 开始的整数数组 answer ，其中：
 * 1、answer.length == nums.length
 * 2、answer[i] = |leftSum[i] - rightSum[i]|
 * 其中：
 * 1、leftSum[i] 是数组 nums 中下标 i 左侧元素之和。如果不存在对应的元素，leftSum[i] = 0 。
 * 2、rightSum[i] 是数组 nums 中下标 i 右侧元素之和。如果不存在对应的元素，rightSum[i] = 0 。
 * 返回数组 answer 。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/left-and-right-sum-differences/
"""
from itertools import accumulate
from typing import List


class Solution:

    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre_sum = [0] + list(accumulate(nums))
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = abs((pre_sum[-1] - pre_sum[i + 1]) - (pre_sum[i]))
        return ans


if __name__ == '__main__':
    # [15,1,11,22]
    print(Solution().leftRightDifference([10, 4, 8, 3]))
    # [0]
    print(Solution().leftRightDifference([1]))