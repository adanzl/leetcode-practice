"""
 * 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。
 * 一开始你有一个空的数组 nums ，你需要 从左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。
 * 每一次插入操作的 代价 是以下两者的 较小值 ：
 * 1、nums 中 严格小于  instructions[i] 的数字数目。
 * 2、nums 中 严格大于  instructions[i] 的数字数目。
 * 比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和  2 小于 3 ，元素 5 大于 3 ），
 * 插入后 nums 变成 [1,2,3,3,5] 。
 * 请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 109 + 7 取余 后返回。
 * 提示：
 * 1、1 <= instructions.length <= 10^5
 * 2、1 <= instructions[i] <= 10^5
 * 链接：https://leetcode.cn/problems/create-sorted-array-through-instructions
"""

import bisect
from typing import List

#
# @lc app=leetcode.cn id=1649 lang=python3
#
# [1649] 通过指令创建有序数组
#


# @lc code=start
class Solution:

    def createSortedArray(self, instructions: List[int]) -> int:
        ans = 0
        arr = []
        for num in instructions:
            il, ir = bisect.bisect_left(arr, num), bisect.bisect_right(arr, num)
            ans += min(len(arr) - ir, il)
            bisect.insort(arr, num)
        return ans % (10**9 + 7)


# @lc code=end

if __name__ == '__main__':
    # 1
    print(Solution().createSortedArray([1, 5, 6, 2]))
    # 3
    print(Solution().createSortedArray([1, 2, 3, 6, 5, 4]))
    # 4
    print(Solution().createSortedArray([1, 3, 3, 3, 2, 4, 2, 1, 2]))
