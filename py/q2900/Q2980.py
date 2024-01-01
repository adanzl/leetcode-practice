"""
 * 你一个 正整数 数组 nums 。
 * 你需要检查是否可以从数组中选出 两个或更多 元素，满足这些元素的按位或运算（ OR）结果的二进制表示中 至少 存在一个尾随零。
 * 例如，数字 5 的二进制表示是 "101"，不存在尾随零，而数字 4 的二进制表示是 "100"，存在两个尾随零。
 * 如果可以选择两个或更多元素，其按位或运算结果存在尾随零，返回 true；否则，返回 false 。
 * 提示：
 * 1、2 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/check-if-bitwise-or-has-trailing-zeros/
"""
from typing import List


class Solution:

    def hasTrailingZeros(self, nums: List[int]) -> bool:
        cnt = 0
        for num in nums:
            if num & 1 == 0:
                cnt += 1
        return cnt >= 2


if __name__ == '__main__':
    # True
    print(Solution().hasTrailingZeros([1, 2, 3, 4, 5]))
    # True
    print(Solution().hasTrailingZeros([2, 4, 8, 16]))
    # False
    print(Solution().hasTrailingZeros([1, 3, 5, 7, 9]))
