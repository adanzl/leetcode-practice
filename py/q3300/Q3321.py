"""
 * 给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。
 * 数组的 x-sum 计算按照以下步骤进行：
 * 1、统计数组中所有元素的出现次数。
 * 2、仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
 * 3、计算结果数组的和。
 * 注意，如果数组中的不同元素少于 x 个，则其 x-sum 是数组的元素总和。
 * 返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的 x-sum。
 * 子数组 是数组内的一个连续 非空 的元素序列。
 * 提示：
 * 1、1 <= n == nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= x <= k <= nums.length
 * 链接：https://leetcode.cn/problems/find-x-sum-of-all-k-long-subarrays-ii/description/
"""
from typing import Counter, List

from sortedcontainers import SortedList

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        L, R = SortedList(), SortedList(key=lambda x: (-x[0], -x[1]))
        sm_l = 0
        cnt = Counter()
        # 对顶堆，解决TOP_K问题
        def add(x):
            nonlocal sm_l
            if [cnt[x], x] in L:
                sm_l -= cnt[x] * x
            L.discard([cnt[x], x])
            R.discard([cnt[x], x])
            cnt[x] += 1
            L.add([cnt[x], x])
            sm_l += cnt[x] * x

        def remove(x):
            nonlocal sm_l
            if [cnt[x], x] in L:
                sm_l -= cnt[x] * x
            L.discard([cnt[x], x])
            R.discard([cnt[x], x])
            cnt[x] -= 1
            if cnt[x]:
                L.add([cnt[x], x])
                sm_l += cnt[x] * x

        def adjust():
            nonlocal sm_l
            while len(L) > x:
                v = L.pop(0)
                R.add(v)
                sm_l -= v[0] * v[1]
            while R and len(L) < x:
                v = R.pop(0)
                L.add(v)
                sm_l += v[0] * v[1]
            while L and R and L[0] < R[0]:
                vl = L.pop(0)
                vr = R.pop(0)
                R.add(vl)
                L.add(vr)
                sm_l -= vl[0] * vl[1]
                sm_l += vr[0] * vr[1]

        ans = []
        for i, num in enumerate(nums):
            add(num)
            if i >= k:
                remove(nums[i - k])
            adjust()
            if i >= k - 1:
                ans.append(sm_l)
        return ans


if __name__ == '__main__':
    # [14,13,11,11,15,17,17]
    print(Solution().findXSum([4, 5, 3, 5, 2, 3, 6, 6, 5, 4], 4, 2))
    # [6,10,12]
    print(Solution().findXSum([1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
    # [13]
    print(Solution().findXSum([9, 2, 2], 3, 3))
    # [11,15,15,15,12]
    print(Solution().findXSum([3, 8, 7, 8, 7, 5], k=2, x=2))
