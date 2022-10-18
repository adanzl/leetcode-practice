"""
 * 给你一个下标从 0 开始的数组 nums ，它含有 n 个非负整数。
 * 每一步操作中，你需要：
 * 1、选择一个满足 1 <= i < n 的整数 i ，且 nums[i] > 0 。
 * 2、将 nums[i] 减 1 。
 * 3、将 nums[i - 1] 加 1 。
 * 你可以对数组执行 任意 次上述操作，请你返回可以得到的 nums 数组中 最大值 最小 为多少。
 * 提示：
 * 1、n == nums.length
 * 2、2 <= n <= 10^5
 * 3、0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimize-maximum-of-array/
"""
from itertools import accumulate
from typing import List
import math


class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        pre_sum = [0] + list(accumulate(nums))
        sm = nums[0]
        cnt = 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:  # reset
                ans = max(ans, min(math.ceil(pre_sum[i] / (i)), math.ceil(sm / cnt)))
                sm = nums[i]
                cnt = 1
            else:
                sm += nums[i]
                cnt += 1
        ans = max(ans, min(math.ceil(pre_sum[-1] / (n)), math.ceil(sm / cnt)))
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().minimizeArrayValue([4, 7, 2, 2, 9, 19, 16, 0, 3, 15]))
    # 5
    print(Solution().minimizeArrayValue([3, 7, 1, 6]))
    # 10
    print(Solution().minimizeArrayValue([10, 1]))
