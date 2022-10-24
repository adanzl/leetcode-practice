"""
 * 在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：
 * 1、令 nums[i] = nums[i] + 2 且
 * 2、令 nums[j] = nums[j] - 2 。
 * 如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。
 * 请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。
 * 提示：
 * 1、n == nums.length == target.length
 * 2、1 <= n <= 10^5
 * 3、1 <= nums[i], target[i] <= 10^6
 * 4、nums 一定可以变得与 target 相似。
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-arrays-similar/
"""
from typing import List


class Solution:

    def makeSimilar(self, nums: List[int], target: List[int]) -> int:

        nums.sort()
        target.sort()
        ans, j = 0, [0, 0]
        for x in nums:
            p = x % 2
            while target[j[p]] % 2 != p:  # 找 target 中奇偶性相同的元素
                j[p] += 1
            ans += abs(x - target[j[p]])
            j[p] += 1
        return ans // 4


if __name__ == '__main__':
    # 2
    print(Solution().makeSimilar([8, 12, 6], [2, 14, 10]))
    # 1
    print(Solution().makeSimilar([1, 2, 5], target=[4, 1, 3]))
    # 0
    print(Solution().makeSimilar([1, 1, 1, 1, 1], target=[1, 1, 1, 1, 1]))
