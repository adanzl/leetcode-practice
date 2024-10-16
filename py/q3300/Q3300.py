"""
 * 给你一个整数数组 nums 。
 * 请你将 nums 中每一个元素都替换为它的各个数位之 和 。
 * 请你返回替换所有元素以后 nums 中的 最小 元素。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 10^4
 * 链接：https://leetcode.cn/problems/minimum-element-after-replacement-with-digit-sum/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def minElement(self, nums: List[int]) -> int:
        ans = INF
        for num in nums:
            vv = 0
            while num:
                vv += num % 10
                num //= 10
            ans = min(ans, vv)
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minElement([10, 12, 13, 14]))
    # 1
    print(Solution().minElement([1, 2, 3, 4]))
    # 10
    print(Solution().minElement([999, 19, 199]))
