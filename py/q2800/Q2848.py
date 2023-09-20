"""
 * 给你一个下标从 0 开始的二维整数数组 nums 表示汽车停放在数轴上的坐标。对于任意下标 i，
 * nums[i] = [start_i, end_i] ，其中 start_i 是第 i 辆车的起点，end_i 是第 i 辆车的终点。
 * 返回数轴上被车 任意部分 覆盖的整数点的数目。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、nums[i].length == 2
 * 3、1 <= start_i <= end_i <= 100
 * 链接：https://leetcode.cn/problems/points-that-intersect-with-cars/
"""
from itertools import accumulate
from typing import List

#
# @lc app=leetcode.cn id=2848 lang=python3
#

# @lc code=start


class Solution:

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # 差分数组
        diff = [0] * 105
        for s, e in nums:
            diff[s] += 1
            diff[e + 1] -= 1
        return sum([1 if v else 0 for v in accumulate(diff)])


# @lc code=end

    def numberOfPoints1(self, nums: List[List[int]]) -> int:
        # 暴力
        ss = set()
        for s, e in nums:
            for i in range(s, e + 1):
                ss.add(i)
        return len(ss)
if __name__ == '__main__':
    # 7
    print(Solution().numberOfPoints([[3, 6], [1, 5], [4, 7]]))
    # 7
    print(Solution().numberOfPoints([[1, 3], [5, 8]]))
