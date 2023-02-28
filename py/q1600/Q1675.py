"""
 * 给你一个由 n 个正整数组成的数组 nums 。
 * 你可以对数组的任意元素执行任意次数的两类操作：
 * 1、如果元素是 偶数 ，除以 2 。例如，如果数组是 [1,2,3,4] ，那么你可以对最后一个元素执行此操作，使其变成 [1,2,3,2]
 * 2、如果元素是 奇数 ，乘上 2 。例如，如果数组是 [1,2,3,4] ，那么你可以对第一个元素执行此操作，使其变成 [2,2,3,4]
 * 数组的 偏移量 是数组中任意两个元素之间的 最大差值 。
 * 返回数组在执行某些操作之后可以拥有的 最小偏移量 。
 * 链接：https://leetcode.cn/problems/minimize-deviation-in-array/
"""
from heapq import heappush, heapreplace
from typing import List


class Solution:

    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        mn = nums[0] * 2
        for num in nums:
            v = num * 2 if num % 2 == 1 else num
            heappush(h, -v)
            mn = min(mn, v)
        ans = -h[0] - mn
        while h and -h[0] % 2 == 0:
            num = -heapreplace(h, h[0] // 2) // 2
            mn = min(mn, num)
            ans = min(ans, -h[0] - mn)
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().minimumDeviation([1, 2, 3, 4]))
    # 3
    print(Solution().minimumDeviation([4, 1, 5, 20, 3]))
    # 3
    print(Solution().minimumDeviation([2, 10, 8]))
