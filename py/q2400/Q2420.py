"""
 * 给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。
 * 对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：
 * 1、下标 i 之前 的 k 个元素是 非递增的 。
 * 2、下标 i 之后 的 k 个元素是 非递减的 。
 * 按 升序 返回所有好下标。
 * 提示：
 * 1、n == nums.length
 * 2、3 <= n <= 10^5
 * 3、1 <= nums[i] <= 10^6
 * 4、1 <= k <= n / 2
 * 链接：https://leetcode.cn/problems/find-all-good-indices/
"""
from typing import *


class Solution:

    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        r = [0] * n
        r[n - 2] = 1
        for i in range(n - 3, 0, -1):
            if nums[i + 2] >= nums[i + 1]:
                r[i] = r[i + 1] + 1
            else:
                r[i] = 1
        pre = 1
        ans = []
        if pre >= k and r[1] >= k:
            ans.append(1)
        for i in range(2, n):
            if nums[i - 2] >= nums[i - 1]:
                pre += 1
            else:
                pre = 1
            if pre >= k and r[i] >= k:
                ans.append(i)
        return ans


if __name__ == '__main__':
    # [2, 3]
    print(Solution().goodIndices([2, 1, 1, 1, 3, 4, 1], 2))
    # []
    print(Solution().goodIndices([2, 1, 1, 2], 2))
