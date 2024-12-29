"""
 * 给你一个长度为 n 的整数数组 nums 和一个二维数组 queries ，其中 queries[i] = [l_i, r_i] 。
 * 每一个 queries[i] 表示对于 nums 的以下操作：
 * 1、将 nums 中下标在范围 [l_i, r_i] 之间的每一个元素 最多 减少 1 。
 * 2、坐标范围内每一个元素减少的值相互 独立 。
 * 零数组 指的是一个数组里所有元素都等于 0 。
 * 请你返回 最多 可以从 queries 中删除多少个元素，使得 queries 中剩下的元素仍然能将 nums 变为一个 零数组 。如果无法将 nums 变为一个 零数组 ，返回 -1 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^5
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i].length == 2
 * 5、0 <= l_i <= r_i < nums.length
 * 链接：https://leetcode.cn/problems/zero-array-transformation-iii/
"""
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify, heapreplace, heappushpop, nlargest, nsmallest
from itertools import zip_longest, product, chain, combinations, combinations_with_replacement, permutations, \
    accumulate, pairwise, count, cycle, repeat, groupby
from functools import reduce, cmp_to_key, cache
from operator import or_, iconcat, and_, xor, mul
from math import inf, gcd, lcm, comb, factorial, isqrt, log2
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda q: q[0])
        h = []
        diff = [0] * (len(nums) + 1)
        sum_d = j = 0
        for i, x in enumerate(nums):
            sum_d += diff[i]
            while j < len(queries) and queries[j][0] <= i:
                heappush(h, -queries[j][1])  # 取相反数表示最大堆
                j += 1
            while sum_d < x and h and -h[0] >= i:
                sum_d += 1
                diff[-heappop(h) + 1] -= 1
            if sum_d < x:
                return -1
        return len(h)


if __name__ == '__main__':
    # 1
    print(Solution().maxRemoval([2, 0, 2], queries=[[0, 2], [0, 2], [1, 1]]))
    # 1
    print(Solution().maxRemoval([1, 1, 1, 1], queries=[[1, 3], [0, 2], [1, 3], [1, 2]]))
    # -1
    print(Solution().maxRemoval([1, 2, 3, 4], queries=[[0, 3]]))
