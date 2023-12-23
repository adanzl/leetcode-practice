"""
 * 给你一个下标从 0 开始的数组 mountain 。你的任务是找出数组 mountain 中的所有 峰值。
 * 以数组形式返回给定数组中 峰值 的下标，顺序不限 。
 * 注意：
 * 1、峰值 是指一个严格大于其相邻元素的元素。
 * 2、数组的第一个和最后一个元素 不 是峰值。
 * 提示：
 * 1、3 <= mountain.length <= 100
 * 2、1 <= mountain[i] <= 100
 * 链接：https://leetcode.cn/problems/find-the-peaks/
"""
from typing import List


class Solution:

    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)
        return ans


if __name__ == '__main__':
    # []
    print(Solution().findPeaks([2, 4, 4]))
    # [1,3]
    print(Solution().findPeaks([1, 4, 3, 8, 5]))
