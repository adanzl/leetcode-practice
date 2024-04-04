"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 一次操作中，你将执行：
 * 1、选择 nums 中最小的两个整数 x 和 y 。
 * 2、将 x 和 y 从 nums 中删除。
 * 3、将 min(x, y) * 2 + max(x, y) 添加到数组中的任意位置。
 * 注意，只有当 nums 至少包含两个元素时，你才可以执行以上操作。
 * 你需要使数组中的所有元素都大于或等于 k ，请你返回需要的 最少 操作次数。
 * 提示：
 * 1、2 <= nums.length <= 2 * 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 10^9
 * 4、输入保证答案一定存在，也就是说一定存在一个操作序列使数组中所有元素都大于等于 k 。
 * 链接：https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/description/
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums and nums[0] < k:
            x, y = heappop(nums), heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            ans += 1
        return ans


if __name__ == '__main__':
    # 2
    print(Solution().minOperations([2, 11, 10, 1, 3], k=10))
    # 4
    print(Solution().minOperations([1, 1, 2, 4, 9], k=20))
