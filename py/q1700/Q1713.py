"""
 * 给你一个数组 target ，包含若干 互不相同 的整数，以及另一个整数数组 arr ，arr 可能 包含重复元素。
 * 每一次操作中，你可以在 arr 的任意位置插入任一整数。
 * 比方说，如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。你可以在数组最开始或最后面添加整数。
 * 请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。
 * 一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。
 * 比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），但 [2,4,2] 不是子序列。
 * 提示：
 * 1、1 <= target.length, arr.length <= 10^5
 * 2、1 <= target[i], arr[i] <= 10^9
 * 3、target 不包含任何重复元素。
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-a-subsequence/
"""

import bisect
from typing import List

#
# @lc app=leetcode.cn id=1713 lang=python3
#
# [1713] 得到子序列的最少操作次数
#


# @lc code=start
class Solution:

    def minOperations(self, target: List[int], arr: List[int]) -> int:
        idx_dic = {}
        for i, num in enumerate(target):
            idx_dic[num] = i
        a = []
        # 转换为求最长递增子序列
        ids = [idx_dic[num] for num in arr if num in idx_dic]
        for ii in ids:
            site = bisect.bisect_left(a, ii)
            if site < len(a):
                a[site] = ii
            else:
                a.append(ii)
        return len(target) - len(a)


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().minOperations([6, 4, 8, 1, 3, 2], arr=[4, 7, 6, 2, 3, 8, 6, 1]))
    # 2
    print(Solution().minOperations([5, 1, 3], arr=[9, 4, 2, 3, 4]))
    #
    # print(Solution().minOperations())
