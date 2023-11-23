"""
 * 给你一个列表 nums ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 nums 中对角线上的整数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i].length <= 10^5
 * 3、1 <= nums[i][j] <= 10^9
 * 4、nums 中最多有 10^5 个数字。
 * 链接：https://leetcode.cn/problems/diagonal-traverse-ii
"""

from typing import List

#
# @lc app=leetcode.cn id=1424 lang=python3
#
# [1424] 对角线遍历 II
#


# @lc code=start
class Solution:

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 二维数组转一维数组
        arr = [[i + j, -i, nums[i][j]] for i in range(len(nums)) for j in range(len(nums[i]))]
        return [v[2] for v in sorted(arr)]


# @lc code=end

if __name__ == '__main__':
    # [1,4,2,7,5,3,8,6,9]
    print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
    print(Solution().findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
    # [1,4,2,5,3,8,6,9,7,10,11]
    print(Solution().findDiagonalOrder([[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]))
    # [1,2,3,4,5,6]
    print(Solution().findDiagonalOrder([[1, 2, 3, 4, 5, 6]]))
