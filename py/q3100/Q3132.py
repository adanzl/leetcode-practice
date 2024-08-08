"""
 * 给你两个整数数组 nums1 和 nums2。
 * 从 nums1 中移除两个元素，并且所有其他元素都与变量 x 所表示的整数相加。
 * 如果 x 为负数，则表现为元素值的减少。
 * 执行上述操作后，nums1 和 nums2 相等 。
 * 当两个数组中包含相同的整数，并且这些整数出现的频次相同时，两个数组 相等 。
 * 返回能够实现数组相等的 最小 整数 x 。
 * 提示：
 * 1、3 <= nums1.length <= 200
 * 2、nums2.length == nums1.length - 2
 * 3、0 <= nums1[i], nums2[i] <= 1000
 * 4、测试用例以这样的方式生成：存在一个整数 x，nums1 中的每个元素都与 x 相加后，再移除两个元素，nums1 可以与 nums2 相等。
 * 链接：https://leetcode.cn/problems/find-the-integer-added-to-array-ii
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=3132 lang=python3
#
# [3132] 找出与数组相加的整数 II
#


# @lc code=start
class Solution:

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1 = Counter(nums1)
        for ans in range(-1000, 1001):
            cnt2 = Counter()
            for num in nums2:
                cnt2[num - ans] += 1
            for v, c in cnt2.items():
                if cnt1[v] < c:
                    break
            else:
                return ans
        return 0

    def minimumAddedInteger1(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        # 枚举保留 nums1[2] 或者 nums1[1] 或者 nums1[0]
        # 倒着枚举是因为 nums1[i] 越大答案越小，第一个满足的就是答案
        for i in range(2, 0, -1):
            x = nums2[0] - nums1[i]
            # 在 {nums1[i] + x} 中找子序列 nums2
            j = 0
            for v in nums1[i:]:
                if nums2[j] == v + x:
                    j += 1
                    # nums2 是 {nums1[i] + x} 的子序列
                    if j == len(nums2):
                        return x
        # 题目保证答案一定存在
        return nums2[0] - nums1[0]


# @lc code=end

if __name__ == '__main__':
    # -1
    print(Solution().minimumAddedInteger([7, 2, 6, 8, 7], [7, 6, 5]))
    # -2
    print(Solution().minimumAddedInteger([4, 20, 16, 12, 8], nums2=[14, 18, 10]))
    # 2
    print(Solution().minimumAddedInteger([3, 5, 5, 3], nums2=[7, 7]))
