"""
 * 给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 
 * 请你返回排序后的数组。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、-100 <= nums[i] <= 100
 * 链接：https://leetcode.cn/problems/sort-array-by-increasing-frequency/
"""
from typing import *


class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for k, v in sorted(cnt.items(), key=lambda x: (x[1], -x[0])):
            ans += [k] * v
        return ans


if __name__ == '__main__':
    # [3,1,1,2,2,2]
    print(Solution().frequencySort([1, 1, 2, 2, 2, 3]))
    # [1,3,3,2,2]
    print(Solution().frequencySort([2, 3, 1, 3, 2]))
    # [5,-1,4,4,-6,-6,1,1,1]
    print(Solution().frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
