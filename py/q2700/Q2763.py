"""
 * 一个长度为 n 下标从 0 开始的整数数组 arr 的 不平衡数字 定义为，在 s_arr = sorted(arr) 数组中，满足以下条件的下标数目：
 * 1、0 <= i < n - 1 ，和
 * 2、s_arr[i+1] - s_arr[i] > 1
 * 这里，sorted(arr) 表示将数组 arr 排序后得到的数组。
 * 给你一个下标从 0 开始的整数数组 nums ，请你返回它所有 子数组 的 不平衡数字 之和。
 * 子数组指的是一个数组中连续一段 非空 的元素序列。
 * 提示：
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= nums.length
 * 链接：https://leetcode.cn/problems/sum-of-imbalance-numbers-of-all-subarrays/
"""
from typing import List
from bisect import bisect_left


class Solution:

    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            lst, cnt = [num], 0
            for ii in range(i - 1, -1, -1):
                idx = bisect_left(lst, nums[ii])
                if idx > 0 and idx < len(lst):
                    if lst[idx] - lst[idx - 1] > 1:
                        cnt -= 1
                if idx <= len(lst) - 1:
                    if lst[idx] - nums[ii] > 1:
                        cnt += 1
                if idx > 0:
                    if nums[ii] - lst[idx - 1] > 1:
                        cnt += 1
                lst.insert(idx, nums[ii])
                ans += cnt
        return ans

    def sumImbalanceNumbers1(self, nums: List[int]) -> int:
        # 贡献法 https://www.bilibili.com/video/BV1ej411m7zV/?spm_id_from=333.999.0.0
        n = len(nums)
        right = [0] * n  # nums[i] 右侧的 x 和 x-1 的最近下标（不存在时为 n）
        idx = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            right[i] = min(idx[x], idx[x - 1])
            idx[x] = i

        ans = 0
        idx = [-1] * (n + 1)
        for i, (x, r) in enumerate(zip(nums, right)):
            # 统计 x 能产生多少贡献
            ans += (i - idx[x - 1]) * (r - i)  # 子数组左端点个数 * 子数组右端点个数
            idx[x] = i
        # 上面计算的时候，每个子数组的最小值必然可以作为贡献，而这是不合法的
        # 所以每个子数组都多算了 1 个不合法的贡献
        return ans - n * (n + 1) // 2


if __name__ == '__main__':
    # 3
    print(Solution().sumImbalanceNumbers([2, 3, 1, 4]))
    # 8
    print(Solution().sumImbalanceNumbers([1, 3, 3, 3, 5]))