"""
 * 给你一个由 正整数 组成的数组 nums 。
 * 返回数组 nums 中所有具有 最大 频率的元素的 总频率 。
 * 元素的 频率 是指该元素在数组中出现的次数。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/count-elements-with-maximum-frequency/
"""
from typing import Counter, List


class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:
        ans = 0
        mx_size = 0
        for v in Counter(nums).values():
            if v > mx_size:
                ans = v
                mx_size = v
            elif v == mx_size:
                ans += v
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]))
    # 5
    print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]))
