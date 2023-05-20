"""
 * 给你一个下标从 0 开始的整数数组 nums ，它表示英雄的能力值。如果我们选出一部分英雄，这组英雄的 力量 定义为：
 * i0 ，i1 ，... ik 表示这组英雄在数组中的下标。那么这组英雄的力量为 max(nums[i0],nums[i1] ... nums[ik])^2 * min(nums[i0],nums[i1] ... nums[ik]) 。
 * 请你返回所有可能的 非空 英雄组的 力量 之和。由于答案可能非常大，请你将结果对 10^9 + 7 取余。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9 
 * 链接：https://leetcode.cn/problems/power-of-heroes/
"""
from typing import List


class Solution:

    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        ans, pre = 0, 0
        for i, v in enumerate(nums):
            pre = pre * 2 + v - (nums[i - 1] if i > 0 else 0)
            ans += pre * v * v
        return ans % (10**9 + 7)


if __name__ == '__main__':
    # 141
    print(Solution().sumOfPower([2, 1, 4]))
    # 3
    print(Solution().sumOfPower([1, 1]))
    # 7
    print(Solution().sumOfPower([1, 1, 1]))
