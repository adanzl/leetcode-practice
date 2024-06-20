"""
 * 车尔尼有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。
 * 两个整数的 数位不同 指的是两个整数 相同 位置上不同数字的数目。
 * 请车尔尼返回 nums 中 所有 整数对里，数位不同之和。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、1 <= nums[i] < 10^9
 * 3、nums 中的整数都有相同的数位长度。
 * 链接：https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/
"""
from typing import Counter, List


class Solution:

    def sumDigitDifferences(self, nums: List[int]) -> int:
        ans = 0
        size = len(str(nums[0]))
        cnt = [Counter() for _ in range(size)]
        for i, num in enumerate(nums):
            for j in range(size):
                v = num // 10**j % 10
                ans += i - cnt[j][v]
                cnt[j][v] += 1
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().sumDigitDifferences([13, 23, 12]))
    # 0
    print(Solution().sumDigitDifferences([10, 10, 10, 10]))
