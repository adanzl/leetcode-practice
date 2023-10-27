"""
 * 矩形蛋糕的高度为 h 且宽度为 w，给你两个整数数组 horizontalCuts 和 verticalCuts，其中：
 * 1、horizontalCuts[i] 是从矩形蛋糕顶部到第  i 个水平切口的距离
 * 2、verticalCuts[j] 是从矩形蛋糕的左侧到第 j 个竖直切口的距离
 * 请你按数组 horizontalCuts 和 verticalCuts 中提供的水平和竖直位置切割后，请你找出 面积最大 的那份蛋糕，并返回其 面积 。
 * 由于答案可能是一个很大的数字，因此需要将结果 对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、2 <= h, w <= 10^9
 * 2、1 <= horizontalCuts.length <= min(h - 1, 10^5)
 * 3、1 <= verticalCuts.length <= min(w - 1, 10^5)
 * 4、1 <= horizontalCuts[i] < h
 * 5、1 <= verticalCuts[i] < w
 * 6、题目数据保证 horizontalCuts 中的所有元素各不相同
 * 7、题目数据保证 verticalCuts 中的所有元素各不相同
 * 链接：https://leetcode.cn/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
"""

from itertools import pairwise
from typing import List

#
# @lc app=leetcode.cn id=1465 lang=python3
#
# [1465] 切割后面积最大的蛋糕
#


# @lc code=start
class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h_arr, v_arr = sorted([0] + horizontalCuts + [h]), sorted([0] + verticalCuts + [w])
        return max([b - a for a, b in pairwise(h_arr)]) * max([b - a for a, b in pairwise(v_arr)]) % (10**9 + 7)


# @lc code=end

if __name__ == '__main__':
    # 4
    print(Solution().maxArea(5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))
    # 6
    print(Solution().maxArea(5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))
    # 9
    print(Solution().maxArea(5, w=4, horizontalCuts=[3], verticalCuts=[3]))
