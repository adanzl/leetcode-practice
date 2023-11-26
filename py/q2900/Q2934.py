"""
 * 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，这两个数组的长度都是 n 。
 * 你可以执行一系列 操作（可能不执行）。
 * 在每次操作中，你可以选择一个在范围 [0, n - 1] 内的下标 i ，并交换 nums1[i] 和 nums2[i] 的值。
 * 你的任务是找到满足以下条件所需的 最小 操作次数：
 * nums1[n - 1] 等于 nums1 中所有元素的 最大值 ，即 nums1[n - 1] = max(nums1[0], nums1[1], ..., nums1[n - 1]) 。
 * nums2[n - 1] 等于 nums2 中所有元素的 最大值 ，即 nums2[n - 1] = max(nums2[0], nums2[1], ..., nums2[n - 1]) 。
 * 以整数形式，表示并返回满足上述 全部 条件所需的 最小 操作次数，如果无法同时满足两个条件，则返回 -1 。
 * 提示：
 * 1、1 <= n == nums1.length == nums2.length <= 1000
 * 2、1 <= nums1[i] <= 10^9
 * 3、1 <= nums2[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-operations-to-maximize-last-elements-in-arrays/
"""
from typing import List


class Solution:

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # plan0
        ans0 = 0
        for i in range(n - 1):
            if nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                ...
            elif nums1[i] <= nums2[-1] and nums2[i] <= nums1[-1]:
                ans0 += 1
            else:
                ans0 = n
                break
        # plan1
        ans1 = 1
        for i in range(n - 1):
            if nums1[i] <= nums2[-1] and nums2[i] <= nums1[-1]:
                ...
            elif nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                ans1 += 1
            else:
                ans1 = n
                break
        ans = min(ans0, ans1)
        return ans if ans != n else -1


if __name__ == '__main__':
    # 1
    print(Solution().minOperations([1, 2, 7], [4, 5, 3]))
    # 2
    print(Solution().minOperations([2, 3, 4, 5, 9], [8, 8, 4, 4, 4]))
    # -1
    print(Solution().minOperations([1, 5, 4], nums2=[2, 5, 3]))
