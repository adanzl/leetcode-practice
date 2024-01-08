"""
 * 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。
 * 回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的欧式距离相等（需要考虑元组的顺序）。
 * 返回平面上所有回旋镖的数量。
 * 提示：
 * 1、n == points.length
 * 2、1 <= n <= 500
 * 3、points[i].length == 2
 * 4、-10^4 <= xi, yi <= 10^4
 * 5、所有点都 互不相同
 * 链接：https://leetcode.cn/problems/number-of-boomerangs
"""

import math
from typing import Counter, List

#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#


# @lc code=start
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            c = Counter()
            for j in points:
                d = math.dist(i, j)
                ans += c[d]
                c[d] += 1
        return ans * 2


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
    # 2
    print(Solution().numberOfBoomerangs([[1, 1], [2, 2], [3, 3]]))
    # 0
    print(Solution().numberOfBoomerangs([[1, 1]]))
