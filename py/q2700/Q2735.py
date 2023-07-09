"""
 * 给你一个长度为 n 、下标从 0 开始的整数数组 nums ，表示收集不同巧克力的成本。
 * 每个巧克力都对应一个不同的类型，最初，位于下标 i 的巧克力就对应第 i 个类型。
 * 在一步操作中，你可以用成本 x 执行下述行为：
 *  同时修改所有巧克力的类型，将巧克力的类型 ith 修改为类型 ((i + 1) mod n)th。
 * 假设你可以执行任意次操作，请返回收集所有类型巧克力所需的最小成本。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= x <= 10^9
 * 链接：https://leetcode.cn/problems/collecting-chocolates/
"""
from typing import List


class Solution:

    def minCost(self, nums: List[int], x: int) -> int:
        INF = int(10**12)
        ans = INF
        n = len(nums)
        min_v = nums[:]

        for s in range(n):
            v = s * x
            for i in range(n):
                min_v[i] = min(min_v[i], nums[(i + s) % n])
            for i, num in enumerate(nums):
                v += min_v[i]
            ans = min(ans, v)
        return ans


if __name__ == '__main__':
    # 13
    print(Solution().minCost([20, 1, 15], x=5))
    # 6
    print(Solution().minCost([1, 2, 3], x=4))