"""
 * 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * 判断你是否能够到达最后一个下标。
 * 提示：
 * 1、1 <= nums.length <= 3 * 10^4
 * 2、0 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/jump-game/description/
"""
from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        n = len(nums)
        for i in range(n):
            if i > mx: break
            mx = max(mx, nums[i] + i)
        return mx >= n - 1


if __name__ == '__main__':
    # True
    print(Solution().canJump([0]))
    # True
    print(Solution().canJump([2, 3, 1, 1, 4]))
    # False
    print(Solution().canJump([3, 2, 1, 0, 4]))
