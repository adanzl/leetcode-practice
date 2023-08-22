"""
 * 给你一个下标从 0 开始长度为 n 的数组 nums 。
 * 每一秒，你可以对数组执行以下操作：
 * 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者 nums[(i + 1) % n] 三者之一。
 * 注意，所有元素会被同时替换。
 * 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。
 * 提示：
 * 1、1 <= n == nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/
"""
from collections import Counter
from typing import List


class Solution:

    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        mx_len = Counter()
        pre_idx = {}
        for i in range(n * 2):
            num = nums[i % n]
            if num in pre_idx:
                l = i - pre_idx[num]
                mx_len[num] = max(mx_len[num], l)
            pre_idx[num] = i
        return min(mx_len.values()) // 2


if __name__ == '__main__':
    # 1
    print(Solution().minimumSeconds([11, 4, 10]))
    # 0
    print(Solution().minimumSeconds([5, 5, 5, 5]))
    # 1
    print(Solution().minimumSeconds([1, 2, 1, 2]))
    # 2
    print(Solution().minimumSeconds([2, 1, 3, 3, 2]))
