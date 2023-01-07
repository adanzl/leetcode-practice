"""
 * 我们定义 arr 是 山形数组 当且仅当它满足：
 * 1、arr.length >= 3
 * 2、存在某个下标 i （从 0 开始） 满足 0 < i < arr.length - 1 且：
 * 3、arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
 * 4、arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
 * 给你整数数组 nums ，请你返回将 nums 变成 山形状数组 的​ 最少 删除次数。
 * 提示：
 * 1、3 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 10^9
 * 3、题目保证 nums 删除一些元素后一定能得到山形数组。
 * 链接：https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/
"""
from typing import List


class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        l_cnt, r_cnt, ans = [1] * n, [1] * n, 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    l_cnt[i] = max(l_cnt[i], l_cnt[j] + 1)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    r_cnt[i] = max(r_cnt[i], r_cnt[j] + 1)
            if 0 < i < n - 1 and l_cnt[i] > 1 and r_cnt[i] > 1:
                ans = max(ans, l_cnt[i] + r_cnt[i] - 1)
        return n - ans


if __name__ == '__main__':
    # 6
    print(Solution().minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]))
    # 0
    print(Solution().minimumMountainRemovals([1, 3, 1]))
    # 2
    print(Solution().minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]))
    # 3
    print(Solution().minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]))
