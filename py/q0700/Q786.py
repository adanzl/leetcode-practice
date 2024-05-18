"""
 * 给你一个按递增顺序排序的数组 arr 和一个整数 k 。数组 arr 由 1 和若干 质数 组成，且其中所有整数互不相同。
 * 对于每对满足 0 <= i < j < arr.length 的 i 和 j ，可以得到分数 arr[i] / arr[j] 。
 * 那么第 k 个最小的分数是多少呢?  以长度为 2 的整数数组返回你的答案, 这里 answer[0] == arr[i] 且 answer[1] == arr[j] 。
 * 提示：
 * 1、2 <= arr.length <= 1000
 * 2、1 <= arr[i] <= 3 * 10^4
 * 3、arr[0] == 1
 * 4、arr[i] 是一个 质数 ，i > 0
 * 5、arr 中的所有数字 互不相同 ，且按 严格递增 排序
 * 6、1 <= k <= arr.length * (arr.length - 1) / 2
 * 链接：https://leetcode.cn/problems/k-th-smallest-prime-fraction
"""

from heapq import heappop, heappush
from typing import List

#
# @lc app=leetcode.cn id=786 lang=python3
#
# [786] 第 K 个最小的质数分数
#


# @lc code=start
class Solution:

    def kthSmallestPrimeFraction1(self, arr: List[int], k: int) -> List[int]:
        vv = []
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                vv.append([arr[i] / arr[j], arr[i], arr[j]])
        val = sorted(vv)[k - 1]
        return [val[1], val[2]]

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = []
        for i in range(n - 1):
            heappush(h, [arr[i] / arr[n-1], i, n-1])
        ans = [0, 0]
        while k:
            v, i0, i1 = heappop(h)
            if i1 > i0:
                heappush(h, [arr[i0] / arr[i1 - 1], i0, i1 - 1])
            ans = [arr[i0], arr[i1]]
            k -= 1
        return ans


# @lc code=end

if __name__ == '__main__':
    # [2,5]
    print(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], k=3))
    # [1,7]
    print(Solution().kthSmallestPrimeFraction([1, 7], k=1))
    #
    # print(Solution().kthSmallestPrimeFraction())
