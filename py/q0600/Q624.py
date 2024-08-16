"""
 * 给定 m 个数组，每个数组都已经按照升序排好序了。
 * 现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。
 * 两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离
 * 注意：
 * 1、每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
 * 2、所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
 * 3、m 个数组中所有整数的范围在 [-10000, 10000] 内。
 * 链接：https://leetcode.cn/problems/maximum-distance-in-arrays
"""

from typing import List

#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624]
#


# @lc code=start
class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:
        arr = sorted([[arr[0], arr[-1], i] for i, arr in enumerate(arrays)])
        arr_end = sorted(arr, key=lambda x: x[1])
        if arr[0][2] != arr_end[-1][2]:
            return arr_end[-1][1] - arr[0][0]
        return max(arr_end[-2][1] - arr[0][0], arr_end[-1][1] - arr[1][0])


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().maxDistance([[-1, 1], [-3, 1, 4], [-2, -1, 0, 2]]))
    # 4
    print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
    # 0
    print(Solution().maxDistance([[1], [1]]))
    # 4
    print(Solution().maxDistance([[1, 4], [0, 5]]))
