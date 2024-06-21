"""
 * 给你一个数组 nums ，数组中的数字 要么 出现一次，要么 出现两次。
 * 请你返回数组中所有出现两次数字的按位 XOR 值，如果没有数字出现过两次，返回 0 。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 3、nums 中每个数字要么出现过一次，要么出现过两次。
 * 链接：https://leetcode.cn/problems/find-the-xor-of-numbers-which-appear-twice
"""
from typing import Counter, List


class Solution:

    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0
        for v, c in Counter(nums).items():
            if c == 2:
                ans ^= v
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().duplicateNumbersXOR([1, 2, 1, 3]))
    # 0
    print(Solution().duplicateNumbersXOR([1, 2, 3]))
    # 3
    print(Solution().duplicateNumbersXOR([1, 2, 2, 1]))
