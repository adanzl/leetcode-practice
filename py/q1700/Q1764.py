"""
 * 给你一个长度为 n 的二维整数数组 groups ，同时给你一个整数数组 nums 。
 * 你是否可以从 nums 中选出 n 个 不相交 的子数组，使得第 i 个子数组与 groups[i] （下标从 0 开始）完全相同，且如果 i > 0 ，那么第 (i-1) 个子数组在 nums 中出现的位置在第 i 个子数组前面。
 * （也就是说，这些子数组在 nums 中出现的顺序需要与 groups 顺序相同）
 * 如果你可以找出这样的 n 个子数组，请你返回 true ，否则返回 false 。
 * 如果不存在下标为 k 的元素 nums[k] 属于不止一个子数组，就称这些子数组是 不相交 的。子数组指的是原数组中连续元素组成的一个序列。
 * 提示：
 * 1、groups.length == n
 * 2、1 <= n <= 10^3
 * 3、1 <= groups[i].length, sum(groups[i].length) <= 10^3
 * 4、1 <= nums.length <= 10^3
 * 5、-10^7 <= groups[i][j], nums[k] <= 10^7
 * 链接：https://leetcode.cn/problems/form-array-by-concatenating-subarrays-of-another-array/
"""
from typing import List


class Solution:

    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i_g, i_n = 0, 0
        gn, nn = len(groups), len(nums)
        while i_g < gn and i_n + len(groups[i_g]) - 1 < nn:
            if groups[i_g] == nums[i_n:i_n + len(groups[i_g])]:
                i_n += len(groups[i_g])
                i_g += 1
            else:
                i_n += 1
        return i_g == gn


if __name__ == '__main__':
    # True
    print(Solution().canChoose([[1, -1, -1], [3, -2, 0]], [1, -1, 0, 1, -1, -1, 3, -2, 0]))
    # False
    print(Solution().canChoose([[10, -2], [1, 2, 3, 4]], [1, 2, 3, 4, 10, -2]))
    # False
    print(Solution().canChoose([[1, 2, 3], [3, 4]], [7, 7, 1, 2, 3, 4, 7, 7]))
