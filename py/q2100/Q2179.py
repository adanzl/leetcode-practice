"""
 * 给你两个下标从 0 开始且长度为 n 的整数数组 nums1 和 nums2 ，两者都是 [0, 1, ..., n - 1] 的 排列 。
 * 好三元组 指的是 3 个 互不相同 的值，且它们在数组 nums1 和 nums2 中出现顺序保持一致。
 * 换句话说，如果我们将 pos1_v 记为值 v 在 nums1 中出现的位置，pos2_v 为值 v 在 nums2 中的位置，
 * 那么一个好三元组定义为 0 <= x, y, z <= n - 1 ，且 pos1_x < pos1_y < pos1_z 和 pos2_x < pos2_y < pos2_z 都成立的 (x, y, z) 。
 * 请你返回好三元组的 总数目 。
 * 提示：
 * 1、n == nums1.length == nums2.length
 * 2、3 <= n <= 10^5
 * 3、0 <= nums1[i], nums2[i] <= n - 1
 * 4、nums1 和 nums2 是 [0, 1, ..., n - 1] 的排列。
 * 链接：https://leetcode.cn/problems/count-good-triplets-in-an-array
"""

import bisect
from typing import List

#
# @lc app=leetcode.cn id=2179 lang=python3
#
# [2179] 统计数组中好三元组数目
#


# @lc code=start
# 树状数组 下标从 1 开始，求和
class BIT:

    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i  # low_bit

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res


class Solution:

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n = len(nums1)
        arr1 = []
        ids1 = [0] * n
        t = BIT(n + 1)
        for i in range(n):
            ids1[nums1[i]] = i
        for num in nums2:
            i1 = ids1[num]
            idx = bisect.bisect(arr1, i1)  # 好二元组个数
            bisect.insort(arr1, i1)
            ans += t.query(i1 + 1)
            t.add(i1 + 1, idx)
        return ans


# @lc code=end

if __name__ == '__main__':
    # 77
    print(Solution().goodTriplets([13, 14, 10, 2, 12, 3, 9, 11, 15, 8, 4, 7, 0, 6, 5, 1],
                                  [8, 7, 9, 5, 6, 14, 15, 10, 2, 11, 4, 13, 3, 12, 1, 0]))
    # 1
    print(Solution().goodTriplets([2, 0, 1, 3], nums2=[0, 1, 2, 3]))
    # 4
    print(Solution().goodTriplets([4, 0, 1, 3, 2], nums2=[4, 1, 0, 2, 3]))
