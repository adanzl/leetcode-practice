"""
 * 给你一个长度为 n 的整数数组 nums 和一个二维数组 queries，其中 queries[i] = [l_i, r_i, val_i]。
 * 每个 queries[i] 表示在 nums 上执行以下操作：
 * 1、将 nums 中 [l_i, r_i] 范围内的每个下标对应元素的值 最多 减少 val_i。
 * 2、每个下标的减少的数值可以独立选择。
 * 零数组 是指所有元素都等于 0 的数组。
 * 返回 k 可以取到的 最小非负 值，使得在 顺序 处理前 k 个查询后，nums 变成 零数组。如果不存在这样的 k，则返回 -1。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 5 * 10^5
 * 3、1 <= queries.length <= 10^5
 * 4、queries[i].length == 3
 * 5、0 <= l_i <= r_i < nums.length
 * 6、1 <= val_i <= 5
 * 链接：https://leetcode.cn/problems/zero-array-transformation-ii
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

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # tree 表示求和
        # set_value(0, 0, n - 1, ii + 1, i, 1)
        tree = [0 for _ in range(2 << n.bit_length())]
        FLAG_DIRTY = -10**9
        # 值可能为0时，dirty设置为-1
        dirty = [FLAG_DIRTY for _ in range(2 << n.bit_length())]

        def push_down(o, l, r):
            if dirty[o] == FLAG_DIRTY: return
            mid = (l + r) >> 1
            set_value(o * 2 + 1, l, mid, l, mid, dirty[o])
            set_value(o * 2 + 2, mid + 1, r, mid + 1, r, dirty[o])
            dirty[o] = FLAG_DIRTY

        def set_value(o, l, r, L, R, val):
            # o: 根节点 l：区间左端点 r：区间右端点 LR：更新下标范围 val：更新值
            mid = (l + r) >> 1
            if l == L and r == R:
                tree[o] += val
                if dirty[o] == FLAG_DIRTY:
                    dirty[o] = val
                else:
                    dirty[o] += val
                return
            push_down(o, l, r)
            if R <= mid:
                set_value(o * 2 + 1, l, mid, L, R, val)
            elif mid + 1 <= L:
                set_value(o * 2 + 2, mid + 1, r, L, R, val)
            else:
                set_value(o * 2 + 1, l, mid, L, mid, val)
                set_value(o * 2 + 2, mid + 1, r, mid + 1, R, val)
            process(o, l, r)

        def query(o, l, r, L, R):
            if l == L and r == R:
                return tree[o]
            push_down(o, l, r)
            mid = (l + r) >> 1
            if R <= mid:
                return query(o * 2 + 1, l, mid, L, R)
            if L >= mid + 1:
                return query(o * 2 + 2, mid + 1, r, L, R)
            return max(query(o * 2 + 1, l, mid, L, mid), query(o * 2 + 2, mid + 1, r, mid + 1, R))

        def process(o, l, r):
            if l == r: return
            a, b = tree[o * 2 + 1], tree[o * 2 + 2]
            tree[o] = max(a, b)

        for i, c in enumerate(nums):
            set_value(0, 0, n - 1, i, i, c)
        ans = 0
        for l, r, val in queries:
            if query(0, 0, n - 1, 0, n - 1) <= 0:
                return ans
            ans += 1
            set_value(0, 0, n - 1, l, r, -val)
        return -1 if query(0, 0, n - 1, 0, n - 1) > 0 else ans


if __name__ == '__main__':
    # 4
    print(Solution().minZeroArray([7,6,8], [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]))
    # 2
    print(Solution().minZeroArray([2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
    # 1
    print(Solution().minZeroArray([5], [[0, 0, 5], [0, 0, 1], [0, 0, 3], [0, 0, 2]]))
    # -1
    print(Solution().minZeroArray([4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))
