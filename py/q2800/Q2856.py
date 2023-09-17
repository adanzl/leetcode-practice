"""
 * 给你一个下标从 0 开始的 非递减 整数数组 nums 。
 * 你可以执行以下操作任意次：
 * 1、选择 两个 下标 i 和 j ，满足 i < j 且 nums[i] < nums[j] 。
 * 2、将 nums 中下标在 i 和 j 处的元素删除。剩余元素按照原来的顺序组成新的数组，下标也重新从 0 开始编号。
 * 请你返回一个整数，表示执行以上操作任意次后（可以执行 0 次），nums 数组的 最小 数组长度。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、nums 是 非递减 数组。
 * 链接：https://leetcode.cn/problems/minimum-array-length-after-pair-removals/
"""
from collections import Counter
from heapq import heapify, heappop, heappush
from typing import List


class Solution:

    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        h = [-c for v, c in cnt.items()]
        heapify(h)
        ans = n
        while len(h) > 1:
            v1, v2 = heappop(h), heappop(h)
            ans -= 2
            if v1 < -1:
                heappush(h, v1 + 1)
            if v2 < -1:
                heappush(h, v2 + 1)
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minLengthAfterRemovals([1, 2, 3, 3, 3]))
    # 1
    print(Solution().minLengthAfterRemovals([1, 3, 3, 3, 4]))
    # 0
    print(Solution().minLengthAfterRemovals([1, 3, 4, 9]))
    # 0
    print(Solution().minLengthAfterRemovals([2, 3, 6, 9]))
    # 1
    print(Solution().minLengthAfterRemovals([1, 1, 2]))
