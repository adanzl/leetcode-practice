from typing import *
"""
 * 给你一个整数数组 nums ，返回出现最频繁的偶数元素。
 * 如果存在多个满足条件的元素，只需要返回 最小 的一个。如果不存在这样的元素，返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 2000
 * 2、0 <= nums[i] <= 10^5
 * 链接：https://leetcode.cn/problems/most-frequent-even-element/
"""


class Solution:

    def mostFrequentEven(self, nums: List[int]) -> int:
        arr = Counter([num for num in nums if num % 2 == 0])
        if len(arr) == 0:
            return -1
        return sorted([[k, v] for k, v in arr.items()], key=lambda x: (-x[1], x[0]))[0][0]


if __name__ == '__main__':
    # 2
    print(Solution().mostFrequentEven([0, 1, 2, 2, 4, 4, 1]))
    # 4
    print(Solution().mostFrequentEven([4, 4, 4, 9, 2, 4]))
    # -1
    print(Solution().mostFrequentEven([29, 47, 21, 41, 13, 37, 25, 7]))
