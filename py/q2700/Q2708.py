"""
 * 给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。
 * 老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的学生下标为 i0, i1, i2, ... , ik ，
 * 那么这个小组的实力值定义为 nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​] 。
 * 请你返回老师创建的小组能得到的最大实力值为多少。
 * 提示：
 * 1、1 <= nums.length <= 13
 * 2、-9 <= nums[i] <= 9
 * 链接：https://leetcode.cn/problems/maximum-strength-of-a-group/
"""
from typing import List


class Solution:

    def maxStrength(self, nums: List[int]) -> int:
        na = []
        c_po, c_zero, c_na = 0, 0, 0
        v_po, v_na = 1, 1
        for v in nums:
            if v > 0:
                v_po *= v
                c_po += 1
            elif v < 0:
                na.append(v)
                v_na *= v
                c_na += 1
            else:
                c_zero += 1
        na.sort()
        if c_na % 2 != 0:
            v_na //= na[-1]
        if c_po: return v_po * v_na
        if c_zero == 0:
            if c_na == 1: return na[0]
            return v_na
        if c_na <= 1: return 0
        return v_na


if __name__ == '__main__':
    # 1350
    print(Solution().maxStrength([3, -1, -5, 2, 5, -9]))
    # 20
    print(Solution().maxStrength([-4, -5, -4]))
    # 0
    print(Solution().maxStrength([0, -1]))
    # 1008
    print(Solution().maxStrength([2, 2, 7, 0, -4, 9, 4]))
    # -9
    print(Solution().maxStrength([-9]))
    # 0
    print(Solution().maxStrength([0]))
