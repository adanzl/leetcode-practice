"""
 * 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，其中 n 是班级中学生的总数。班主任希望能够在让所有学生保持开心的情况下选出一组学生：
 * 如果能够满足下述两个条件之一，则认为第 i 位学生将会保持开心：
 * 1、这位学生被选中，并且被选中的学生人数 严格大于 nums[i] 。
 * 2、这位学生没有被选中，并且被选中的学生人数 严格小于 nums[i] 。
 * 返回能够满足让所有学生保持开心的分组方法的数目。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] < nums.length
 * 链接：https://leetcode.cn/problems/happy-students/
"""
from typing import List


class Solution:

    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 1 if 0 < nums[0] else 0
        for i in range(n - 1):
            if nums[i] < i + 1 and nums[i + 1] > i + 1:
                ans += 1
        if nums[-1] < n:
            ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().countWays([1, 1]))
    # 3
    print(Solution().countWays([6, 0, 3, 3, 6, 7, 2, 7]))
