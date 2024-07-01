"""
 * 给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况
 * 如果存在，请返回 true ；否则，返回 false 。
 * 提示：
 * 1、1 <= arr.length <= 1000
 * 2、1 <= arr[i] <= 1000
 * 链接：https://leetcode.cn/problems/three-consecutive-odds
"""

from typing import List

#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#


# @lc code=start
class Solution:

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for num in arr:
            if num & 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3: return True
        return False


# @lc code=end

if __name__ == '__main__':
    # False
    print(Solution().threeConsecutiveOdds([2, 6, 4, 1]))
    # True
    print(Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
