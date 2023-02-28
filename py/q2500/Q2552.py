"""
 * 给你一个长度为 n 下标从 0 开始的整数数组 nums ，它包含 1 到 n 的所有数字，请你返回上升四元组的数目。
 * 如果一个四元组 (i, j, k, l) 满足以下条件，我们称它是上升的：
 * 1、0 <= i < j < k < l < n 且
 * 2、nums[i] < nums[k] < nums[j] < nums[l] 。
 * 提示：
 * 1、4 <= nums.length <= 4000
 * 2、1 <= nums[i] <= nums.length
 * 3、nums 中所有数字 互不相同 ，nums 是一个排列。
 * 链接：https://leetcode.cn/problems/count-increasing-quadruplets/
"""
from typing import List


class Solution:

    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        great = [[]] * n
        great[-1] = [0] * (n + 1)
        for k in range(n - 2, 1, -1):
            great[k] = great[k + 1][:]
            for x in range(1, nums[k + 1]):
                great[k][x] += 1  # x < nums[k+1]，对于 x，大于它的数的个数 +1

        ans = 0
        less = [0] * (n + 1)
        for j in range(1, n - 1):
            for x in range(nums[j - 1] + 1, n + 1):
                less[x] += 1  # x > nums[j-1]，对于 x，小于它的数的个数 +1
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    ans += less[nums[k]] * great[k][nums[j]]
        return ans

    def countQuadruplets1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        cnt = [0] * n
        for i in range(n):
            large = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    ans += cnt[j]
                    large += 1
                else:
                    cnt[j] += large

        return ans


if __name__ == '__main__':
    # 7
    print(Solution().countQuadruplets([3, 9, 5, 4, 8, 2, 1, 10, 7, 6]))
    # 2
    print(Solution().countQuadruplets([1, 3, 2, 4, 5]))
    # 0
    print(Solution().countQuadruplets([1, 2, 3, 4]))
