"""
 * 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：
 * 1、left 中的每个元素都小于或等于 right 中的每个元素。
 * 2、left 和 right 都是非空的。
 * 3、left 的长度要尽可能小。
 * 在完成这样的分组后返回 left 的 长度 。
 * 用例可以保证存在这样的划分方法。
 * 提示：
 * 1、2 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^6
 * 3、可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。
 * 链接：https://leetcode.cn/problems/partition-array-into-disjoint-intervals/
"""
from typing import List


class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        r_min = [0x3c3c3c3c] * n
        r_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            r_min[i] = min(nums[i], r_min[i + 1])
        l_mx = nums[0]
        for i in range(1, n):
            if l_mx <= r_min[i]:
                return i
            l_mx = max(l_mx, nums[i])
        return 0


if __name__ == '__main__':
    # 3
    print(Solution().partitionDisjoint([5, 0, 3, 8, 6]))
    # 4
    print(Solution().partitionDisjoint([1, 1, 1, 0, 6, 12]))
