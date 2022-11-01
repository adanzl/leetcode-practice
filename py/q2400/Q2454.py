"""
 * 给你一个下标从 0 开始的非负整数数组 nums 。对于 nums 中每一个整数，你必须找到对应元素的 第二大 整数。
 * 如果 nums[j] 满足以下条件，那么我们称它为 nums[i] 的 第二大 整数：
 * 1、j > i
 * 2、nums[j] > nums[i]
 * 3、恰好存在 一个 k 满足 i < k < j 且 nums[k] > nums[i] 。
 * 如果不存在 nums[j] ，那么第二大整数为 -1 。
 * 比方说，数组 [1, 2, 4, 3] 中，1 的第二大整数是 4 ，2 的第二大整数是 3 ，3 和 4 的第二大整数是 -1 。
 * 请你返回一个整数数组 answer ，其中 answer[i]是 nums[i] 的第二大整数。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/next-greater-element-iv/
"""
from bisect import bisect_right, insort
from typing import List


class Solution:

    def secondGreaterElement1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        arr = []
        # 名次树
        for num, i in sorted([[num, i] for num, i in zip(nums, range(n))], key=lambda x: (-x[0], x[1])):
            idx = bisect_right(arr, i, key=lambda x: x[0])
            if idx <= len(arr) - 2: ans[i] = arr[idx + 1][1]
            insort(arr, [i, num], key=lambda x: x[0])
        return ans

    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        h_zero, h_one = [], []
        # 两次单调栈
        for i, num in enumerate(nums):
            while h_one and nums[h_one[-1]] < num:
                ans[h_one.pop()] = num
            idx = len(h_zero) - 1
            while idx >= 0 and nums[h_zero[idx]] < num:
                idx -= 1
            h_one += h_zero[idx + 1:]
            del h_zero[idx + 1:]
            h_zero.append(i)
        return ans


if __name__ == '__main__':
    # [15,15,-1,-1,12,-1,-1,-1,-1]
    print(Solution().secondGreaterElement([11, 13, 15, 12, 0, 15, 12, 11, 9]))
    # [9,6,6,-1,-1]
    print(Solution().secondGreaterElement([2, 4, 0, 9, 6]))
    # [-1,-1]
    print(Solution().secondGreaterElement([3, 3]))
    # [18,18,-1,10,-1,-1,-1,-1]
    print(Solution().secondGreaterElement([1, 17, 18, 0, 18, 10, 20, 0]))
