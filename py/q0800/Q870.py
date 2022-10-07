"""
 * 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
 * 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。
 * 提示：
 * 1、1 <= nums1.length <= 10^5
 * 2、nums2.length == nums1.length
 * 3、0 <= nums1[i], nums2[i] <= 10^9
 * 链接：https://leetcode.cn/problems/advantage-shuffle/
"""
from typing import List


class Solution:

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        ans = [0] * n
        nums1.sort()
        arr = sorted(zip(nums2, range(n)))
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if arr[i][0] >= nums1[r]:
                ans[arr[i][1]] = nums1[l]
                l += 1
            else:
                ans[arr[i][1]] = nums1[r]
                r -= 1
        return ans


if __name__ == '__main__':
    # [2,11,7,15]
    print(Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
    # [24,32,8,12]
    print(Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
