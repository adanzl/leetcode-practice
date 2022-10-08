"""
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
 * 返回这三个数的和。假定每组输入只存在唯一答案。
 * 提示：
 * 1、3 <= nums.length <= 1000
 * 2、-1000 <= nums[i] <= 1000
 * 3、-10^4 <= target <= 10^4
 * 链接：https://leetcode-cn.com/problems/3sum-closest
"""
from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0x3c3c3c3c
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, n - 1
            sm = nums[i] + nums[n - 1] + nums[n - 2]
            if sm < target:
                #  largest sum is smaller than target
                ans = sm
                continue
            sm = nums[i] + nums[i + 1] + nums[i + 2]
            if sm > target:
                #  smallest sum is larger than target
                if sm - target < abs(ans - target):
                    ans = sm
                break
            while l < r:
                sm = nums[l] + nums[r] + nums[i]
                if sm == target: return target
                if sm > target:
                    r -= 1
                else:
                    l += 1

                if abs(sm - target) < abs(ans - target):
                    ans = sm
        return ans


if __name__ == '__main__':
    # 291
    print(Solution().threeSumClosest([
        40, -53, 36, 89, -38, -51, 80, 11, -10, 76, -30, 46, -39, -15, 4, 72, 83, -25, 33, -69, -73, -100, -23, -37, -13, -62, -26, -54, 36, -84, -65, -51, 11, 98, -21, 49, 51, 78, -58, -40, 95, -81,
        41, -17, -70, 83, -88, -14, -75, -10, -44, -21, 6, 68, -81, -1, 41, -61, -82, -24, 45, 19, 6, -98, 11, 9, -66, 50, -97, -2, 58, 17, 51, -13, 88, -16, -77, 31, 35, 98, -2, 0, -70, 6, -34, -8,
        78, 22, -1, -93, -39, -88, -77, -65, 80, 91, 35, -15, 7, -37, -96, 65, 3, 33, -22, 60, 1, 76, -32, 22
    ], 292))
    # 3
    print(Solution().threeSumClosest([1, 1, 1, 1], 0))
    # 2
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    # 0
    print(Solution().threeSumClosest([0, 0, 0], 1))
